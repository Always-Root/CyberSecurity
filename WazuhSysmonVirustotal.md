## What is Wazuh?
Wazuh is a security platform that provides unified XDR (Extended Detection and Response) and SIEM protection for endpoints and cloud workloads. Wazuh is free and open source.

## We need to setup Wazuh for file integrity and malware detection
To achieve this goal, we need to setup and install the following: 
1.	Setting up Wazuh on virtual box and Accessing the Wazuh dashboard
2.	Install Wazuh agent on endpoint(windows 10)
3.	Install Sysmon on endpoint (windows 10) device. Integrate Sysmon logs to Wazuh agent
4.	File integrity (file creation, modification and deletion will be triggered on Wazuh server)
5.	Connecting with total virus to detect malicious payloads


## Setting up Wazuh server on virtual box Accessing the Wazuh dashboard::
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
*	Download Wazuh GUI agent for window 10  (https://packages.wazuh.com/4.x/windows/wazuh-agent-4.14.0-1.msi).
*	Change the manager IP filed with your Wazuh server IP
<img width="799" height="446" alt="Image" src="https://github.com/user-attachments/assets/79068ec7-8f4a-4b29-b7fa-d1ef7a03a906" />

