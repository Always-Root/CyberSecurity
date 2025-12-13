# Security Auditing of a website
### We will be pentesting OWASP Juice Shop (https://juice-shop.herokuapp.com/#/) and DVWA; We don't have permission to pentest such as internee.pk.
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
```
sudo apt install dvwa
```

## 2. Automated Scanning with OWASP ZAP to Find Vulnerabilities in the Application
* Open OWASF ZAP by executing ```owasf-zap``` in the terminal
* For a quick and easy scan, click on Automated Scan and enter the URL you want to test and click on Attack button.
* After the scan completes, open the Alerts tab to view all detected vulnerabilities categorized by severity.
* You can generate a report by going to Report and choosing the desired format from there
<img width="1353" height="686" alt="VirtualBoxVM_EYhQxhIrS3" src="https://github.com/user-attachments/assets/7c20e23d-2b1a-4aa5-9bc4-e5a64ef858f4" />

## 3. SQL injection attack with sqlmap
* To perform sql injection start dvwa with ```dvwa-start```
* Navigate to your locally dvwa login page Username ```admin```  Password ```password```
* Set DVWA Security level to Low under the “DVWA Security” tab and reset the database
* Go to the “SQL Injection” section in the input box (User ID), enter any number like 1 and click Submit
* Then go to Inspect > Network tab > cookies tab and copy PHPSESSID vlue, and change it with your one in the below command
```
sudo sqlmap "http://127.0.0.1:42001/vulnerabilities/sqli/?id=1&Submit=Submit#" --cookie="PHPSESSID=1ba614ae0bf93c5af4789cead27e0d02;security=low" -D dvwa - T users --columns
```
<img width="1366" height="716" alt="2" src="https://github.com/user-attachments/assets/c0a057a4-dafb-41a1-a27f-e63f58743e4c" />

