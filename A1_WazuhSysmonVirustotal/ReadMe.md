## What is Wazuh?
Wazuh is a security platform that provides unified XDR (Extended Detection and Response) and SIEM protection for endpoints and cloud workloads. Wazuh is free and open source.


## What is Sysmon?
A free Windows service and driver from Microsoft Sysinternals.  
It records detailed system activity, such as:
- Process creation
- Network connections
- File changes  
All logs are written to the Windows Event Log, which can then be forwarded to Wazuh for analysis.



## What is VirusTotal?
is a free online service that analyzes suspicious files, URLs, domains, and IP addresses to detect malware and other malicious content using dozens of antivirus engines


## Project Objectives
The goal of this project is to:
1. Deploy a Wazuh server in a virtual environment.  
2. Install and connect a Wazuh Agent on a Windows 10 endpoint.  
3. Install Sysmon and forward its logs to the Wazuh server.  
4. Configure **File Integrity Monitoring (FIM)** to detect file creation, modification, and deletion.  
5. Integrate VirusTotal for basic malware detection.

## Tools and Requirements
| Tool | Purpose |
|------|----------|
| **VirtualBox** | To run the Wazuh server VM |
| **Windows 10** | Endpoint device to install Wazuh Agent and Sysmon |
| **Wazuh** | EDR & SIEM platform |
| **Sysmon** | Collects detailed Windows logs |
| **VirusTotal API** | For file hash analysis and malware detection |
| **PowerShell** | Installation and service management |



## Setting up Wazuh server on virtual box and Accessing the Wazuh dashboard::
* Download the Wazuh ova file (https://packages.wazuh.com/4.x/vm/wazuh-4.14.0.ova)
* Google it “How to install ova file on virtual box” if you don’t know
* When the ova file installation finish, login the Wazuh server the username is “wazuh-user” and password is “wazuh”
*	Type ``` ip a ```  command and copy the Wazuh server IP address
<img width="1079" height="651" alt="Image" src="https://github.com/user-attachments/assets/dfcce862-576e-4113-ba4c-60aaea77b2d8" />

*	Open the browser and paste the Wazuh server IP with https.
*	Login to the Wazuh dashboard by using the admin and admin.
<img width="1060" height="562" alt="Image" src="https://github.com/user-attachments/assets/139a3a7f-db2e-4d0b-b805-18b87bd975f3" />
<img width="1360" height="687" alt="Image" src="https://github.com/user-attachments/assets/8c346cd4-c031-4c0e-a4ef-09dd41d321fe" />

*	And enjoy the beautiful Wazuh interface, are we done? no, no there is a lot to do.




## Install Wazuh agent on endpoint(windows 10):
*	Copy the below command and paste in the powershell with adminstartive privileges, change the IP with your one in the command.
```Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.14.0-1.msi -OutFile $env:tmp\wazuh-agent; msiexec.exe /i $env:tmp\wazuh-agent /q WAZUH_MANAGER='192.168.0.109' ```
*	Change the manager IP filed variable with your Wazuh server IP
*	Then run this commannd ```NET START Wazuh``` to start the wazuh agent
*	Apply the same to the GUI agent if you want.
<img width="799" height="446" alt="Image" src="https://github.com/user-attachments/assets/79068ec7-8f4a-4b29-b7fa-d1ef7a03a906" />


*	Once the connection made you will see the agents in the endpoint devices by clicking on it
<img width="1349" height="597" alt="Image" src="https://github.com/user-attachments/assets/cf960fe9-aa2f-4d78-b8c4-2f0c55b92ee9" />


## Install Sysmon on endpoint (windows 10) device. Integrate Sysmon logs to Wazuh agent
* Download Sysmon from the official website ```https://download.sysinternals.com/files/Sysmon.zip``` and extract it
* Install by executing ```.\Sysmon.exe -i -accepteula``` within the extracted directory by using powershell with Administrative privileges
* It will install and up itselp and start logging
* Open Notepad with Adminstrative privileges and open the Wazuh agent configuration file with in this directory ```C:\Program Files (x86)\ossec-agent\ossec.conf```
* To get logs from sysmon and send to Wazuh server we need add a few lines of code to ossec.conf file
```
<localfile>
    <location>Microsoft-Windows-Sysmon/Operational</location>
    <log_format>eventchannel</log_format>
</localfile>
```
* Add this code to ossec.conf in the directory portion like its shown below:
<img width="1360" height="768" alt="notepad_a0cXmExAfB" src="https://github.com/user-attachments/assets/42975c9e-5bc7-4477-8662-8e2b0a38114c" />

* Run these commands ```net stop wazuh``` and ```net start wazuh```
* Once it done all the sysmon logs will be sent to Wazuh dashboard


## File integrity monitring or FIM with Wazuh
* Open the ossec.conf file and add the following line of code and the change USERNAME with your one
  ```
  <directories check_all="yes" report_changes="yes" realtime="yes">C:\Users\USERNAME\Desktop</directories>
  ```
  <img width="1360" height="728" alt="notepad_6UpkUeTCWr" src="https://github.com/user-attachments/assets/704a61c5-ccd9-4701-bedd-1d3511a64497" />
* Once it done correctly file creation, modification and deletion will be trigged on the Wazuh dashboard as shown below
<img width="1360" height="641" alt="chrome_ID6JxYjUq2" src="https://github.com/user-attachments/assets/6dca10cc-fe63-406c-960d-1c98443ee782" />

## VirusTotal integration
* This integration uses the VirusTotal API to detect malicious content within the files and directories monitored by the File Integrity Monitoring(FIM) in our case the path is ```C:\Users\USERNAME\Desktop```
* lets install mimikatz on our desktop (mimikatz is considred is a malacious file)
<img width="1360" height="641" alt="chrome_VitVVzOEvD" src="https://github.com/user-attachments/assets/cd5eb9ce-5e2b-4c2c-b5ce-a0ed116bf33d" />

* when you execute the mimikatz.exe it will be triggred on Threat Huntaing events on your Wazuh dashboard

<img width="1360" height="662" alt="notepad_nJJL9opJD6" src="https://github.com/user-attachments/assets/426f0d7d-2da9-4cc8-a02c-176c5ce75ff3" />


⚠️ **Note:** This was a project and may only be used for learning purpose. 



