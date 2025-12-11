# Security Auditing of a website
### We will be pentesting OWASP Juice Shop (https://juice-shop.herokuapp.com/#/); We don't have permission to pentest such as internee.pk.
### OWASF Juice Shop is a insecure web application and it can be used in security trainings.

## 1. Fire up your Kali linux and execute the following commands:
```
sudo apt update
```
```
sudo apt install zaproxy
```
```
sudo apt install nodejs
```
```
sudo apt install npm
```

## 2. Automated Scanning with OWASP ZAP to Find Vulnerabilities in the Application
* Open OWASF ZAP by executing ```owasf-zap``` in the terminal
* For a quick and easy scan, click on Automated Scan and enter the URL you want to test and click on Attack button.
* After the scan completes, open the Alerts tab to view all detected vulnerabilities categorized by severity.
* You can generate a report by going to Report and choosing the desired format from there
<img width="1353" height="686" alt="VirtualBoxVM_EYhQxhIrS3" src="https://github.com/user-attachments/assets/7c20e23d-2b1a-4aa5-9bc4-e5a64ef858f4" />

## 3. SQL injection attack with sqlmap
* To perform sql injection we need install OWASP Juice Shop locally
* Install OWASP Juice Shop locally from git hub and change to that directory follow the commands
* ```git clone https://github.com/juice-shop/juice-shop.git``` ```cd juice-shop```
* inside the juice directory execute ```npm install``` and ```npm start``` now the app is running on 300 port
