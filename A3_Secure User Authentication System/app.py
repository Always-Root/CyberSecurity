from flask import (
    Flask,
    render_template,
    url_for,
    request,
    redirect,
    flash,
    session,
    send_file,
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from sqlalchemy import text
from werkzeug.security import generate_password_hash, check_password_hash

import pyotp
import qrcode
import io
import sqlite3

db = SQLAlchemy()
login_manager = LoginManager()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # 2FA fields
    twofa_secret = db.Column(db.String(32), nullable=True)
    is_twofa_enabled = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<User {self.username}>"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "my-sec-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "login"

    with app.app_context():
        db.create_all()

    # --------------------------------------------------------------
    # HEALTH CHECK ROUTE
    # --------------------------------------------------------------
    @app.route("/health/db")
    def health_db():
        try:
            db.session.execute(text("SELECT 1"))
            return {"db": "ok"}, 200
        except Exception as e:
            return { "error": str(e) }, 500

    # --------------------------------------------------------------
    # BASIC ROUTES
    # --------------------------------------------------------------
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/dashboard")
    @login_required
    def dashboard():
        return render_template("dashboard.html")

    # --------------------------------------------------------------
    # REGISTER
    # --------------------------------------------------------------
    @app.route("/register", methods=["GET", "POST"])
    def register():
        if request.method == "POST":
            username = (request.form.get("username") or "").strip()
            email = (request.form.get("email") or "").strip().lower()
            password = request.form.get("password") or ""

            # Basic validation
            if not username or not email or not password:
                flash("Username, email and password are required.", "warning")
                return render_template("register.html")

            if len(password) < 6:
                flash("Password must be at least 6 characters.", "warning")
                return render_template("register.html")

            # Prevent duplicate email / username
            if User.query.filter((User.email == email) | (User.username == username)).first():
                flash("A user with that email or username already exists.", "danger")
                return render_template("register.html")

            try:
                password_hash = generate_password_hash(password)
                secret = pyotp.random_base32()

                user = User(
                    username=username,
                    email=email,
                    password_hash=password_hash,
                    twofa_secret=secret,
                    is_twofa_enabled=False,
                )

                db.session.add(user)
                db.session.commit()

                # Log the user in immediately so they can set up 2FA
                login_user(user)

                flash("Account created! Please set up 2FA.", "success")
                return redirect(url_for("setup_2fa", user_id=user.id))

            except Exception as e:
                # If the DB schema doesn't match (old DB), give a hint
                flash("Error creating account: " + str(e), "danger")

        return render_template("register.html")

    # --------------------------------------------------------------
    # LOGIN + 2FA STEP
    # --------------------------------------------------------------
    @app.route("/login", methods=["GET", "POST"])
    def login():
        errors = []

        if request.method == "POST":
            email = (request.form.get("email") or "").strip().lower()
            password = request.form.get("password") or ""

            if not email or not password:
                flash("Email and password are required.", "warning")
                return render_template("login.html", errors=errors)

            user = User.query.filter_by(email=email).first()

            if not user:
                flash("No account found with that email.", "danger")
                return render_template("login.html", errors=errors)

            if not check_password_hash(user.password_hash, password):
                flash("Incorrect password.", "danger")
                return render_template("login.html", errors=errors)

            # Save user ID for 2FA verification step
            session["2fa_user_id"] = user.id

            # If they already enabled 2FA → go to OTP page
            if user.is_twofa_enabled:
                return redirect(url_for("verify_2fa"))

            # Otherwise → they must set up 2FA (user is logged in by this point)
            # We can also log them in now, but we require they finish setup to use dashboard.
            login_user(user)
            return redirect(url_for("setup_2fa", user_id=user.id))

        return render_template("login.html", errors=errors)

    # --------------------------------------------------------------
    # GENERATE QR CODE FOR GOOGLE AUTHENTICATOR
    # --------------------------------------------------------------
    @app.route("/qr/<int:user_id>")
    @login_required
    def qr_code(user_id):
        # Only allow the logged-in user to fetch their own QR
        if current_user.id != user_id:
            return ("Forbidden", 403)

        user = User.query.get_or_404(user_id)
        totp = pyotp.TOTP(user.twofa_secret)

        uri = totp.provisioning_uri(
            name=user.email,
            issuer_name="CyberSecurityApp"
        )

        qr = qrcode.make(uri)
        img_io = io.BytesIO()
        qr.save(img_io, "PNG")
        img_io.seek(0)

        return send_file(img_io, mimetype="image/png")

    # --------------------------------------------------------------
    # SETUP 2FA (INITIAL)
    # --------------------------------------------------------------
    @app.route("/setup-2fa/<int:user_id>", methods=["GET", "POST"])
    @login_required
    def setup_2fa(user_id):
        # ensure only the logged-in user can configure their own 2FA
        if current_user.id != user_id:
            flash("You are not authorized to set up 2FA for this account.", "danger")
            return redirect(url_for("index"))

        user = User.query.get_or_404(user_id)

        if request.method == "POST":
            otp = request.form.get("otp") or ""
            totp = pyotp.TOTP(user.twofa_secret)

            if totp.verify(otp):
                user.is_twofa_enabled = True
                db.session.commit()

                flash("2FA enabled successfully!", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid OTP. Try again.", "danger")

        return render_template("setup_2fa.html", user=user)

    # --------------------------------------------------------------
    # VERIFY 2FA DURING LOGIN
    # --------------------------------------------------------------
    @app.route("/verify-2fa", methods=["GET", "POST"])
    def verify_2fa():
        user_id = session.get("2fa_user_id")

        if not user_id:
            flash("Session expired. Login again.", "warning")
            return redirect(url_for("login"))

        user = User.query.get(user_id)
        if not user:
            flash("User not found. Login again.", "warning")
            return redirect(url_for("login"))

        if request.method == "POST":
            otp = request.form.get("otp") or ""
            totp = pyotp.TOTP(user.twofa_secret)

            if totp.verify(otp):
                login_user(user)
                session.pop("2fa_user_id", None)
                flash("Logged in successfully.", "success")
                return redirect(url_for("dashboard"))
            else:
                flash("Invalid code. Try again.", "danger")

        return render_template("verify_2fa.html")

    # --------------------------------------------------------------
    # LOGOUT
    # --------------------------------------------------------------
    @app.route("/logout")
    def logout():
        logout_user()
        flash("Logged out successfully", "success")
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=9999)
