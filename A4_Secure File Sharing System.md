# Creating a Secure File Sharing System with FileGator
## Exchanges files between internal and external parties.

1. Fire up your fresh ubuntu LTS server/desktop and run the following commands one by one:
```
sudo su
```
```
apt update
```
```
apt install -y wget unzip php apache2 libapache2-mod-php php-zip php-mbstring php-dom php-xml
```

```
apt install apache2
```
```
cd /var/www/
```
```
wget https://github.com/filegator/static/raw/master/builds/filegator_latest.zip
```
```
unzip filegator_latest.zip && rm filegator_latest.zip
```
```
chown -R www-data:www-data filegator/
```
```
chmod -R 775 filegator/
```
```
echo "
<VirtualHost *:80>
    DocumentRoot /var/www/filegator/dist
</VirtualHost>
" >> /etc/apache2/sites-available/filegator.conf
```
```
a2dissite 000-default.conf
```
```
a2ensite filegator.conf
```
```
systemctl restart apache2
```

2. When the installation finshed type ```ifconfig``` and copy your IP from the terminal and paste it into your favrite browser.
* Login window will appear just enter username ```admin``` password ```admin123```
* Now you are good to to create, upload, delete and share files

```

