# Security Auditing of a website
### We will pentesting OWASP Juice Shop (https://juice-shop.herokuapp.com/#/); We don't have permission to pentest such as internee.pk.
### OWASF Juice Shop is a insecure web application and it can be used in security trainings.

## 1. Fire up your Kali linux and execute the following commands:
```
sudo apt update
```
```
sudo apt install zaproxy
```

## Automated Scanning with OWASP ZAP to Find Vulnerabilities in the Application
* Open OWASF ZAP by executing ```owasf-zap``` in the terminal
* For a quick and easy scan, click on Automated Scan and enter the URL you want to test.
* After the scan completes, open the Alerts tab to view all detected vulnerabilities categorized by severity.
* You can generate a report by going to Report and choosing the desired format from there
