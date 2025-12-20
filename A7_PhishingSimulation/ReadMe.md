## Phishing simulation attack with Gophish
A phishing simulation is a cybersecurity exercise that tests an organization's ability to recognize and respond to a phishing attack.


1. To do that, fire up your Kali Linux
2. Execute ```sudo gophish``` in the terminal, and it will provide the default user, pass and web UI IP

3. Login with default credentials
<img width="893" height="595" alt="1" src="https://github.com/user-attachments/assets/5501e0ea-23cf-4848-b62e-13c6136c09a5" />

4. Set up new passwords
<img width="903" height="602" alt="2" src="https://github.com/user-attachments/assets/e430cfa3-e19f-4e7a-89b6-83dd62cbbbab" />

5. Lets set up email server for sending emails in our case it will be smtp.gmail.com
   * Login to your gmail account and click on Manage Account, search for App Passwords, create one and copy
<img width="1034" height="560" alt="3" src="https://github.com/user-attachments/assets/f64593c1-20e0-4a1b-9a6c-7302388fa9b3" />

  
6. Click on Sending Profiles > New Profile
   * Fill as shown below and put that password in the password field you recently copied then click Save Profile
<img width="341" height="511" alt="4" src="https://github.com/user-attachments/assets/1c4abfde-5ecc-40e5-a7c0-f5317ec27f1b" />

6. Click on Landing Pages > New Page
   * Choose name of the template
   * Open the google login template which reside ```/usr/share/set/src/html/templates/google/index.html``` and paste it in the template box
   * check capture data/password and Click Save Page
<img width="354" height="502" alt="5" src="https://github.com/user-attachments/assets/8577b1f6-dc82-4ebb-ba98-cae7cf0055f6" />

7. Click on Email Templates > New Template
   * Fill as shown below or fill according to your choice
   * The template configuration also includes an option for “Add Tracking Image” for capture “Email Opened” metrics
<img width="350" height="523" alt="6" src="https://github.com/user-attachments/assets/25aaa1af-a846-4eb5-9763-c68b9b9287d6" />

8. Click on User & Groups > New Group
   * Add your targets to GoPhish by creating a new group
   * You can import users through a comma-delimited CSV file or manually enter their information and click Save Changes
<img width="900" height="600" alt="7" src="https://github.com/user-attachments/assets/848a0488-71c1-48a0-9e7d-5d6718c3fdc9" />

9. Launch Campaign
   * Create a new Campaign under Campaigns > New Campaign
   * Configure your Campaign with the appropriate Email Template, Landing Page, and Sending Profile. The configured URL will be the GoPhish server URL that hosts the Landing Page and “Email Opened” image tracker
<img width="843" height="562" alt="8" src="https://github.com/user-attachments/assets/cb541270-9259-4bac-b8f5-5516fd55fed6" />


