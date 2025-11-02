## What is Wazuh?
Wazuh is a security platform that provides unified XDR (Extended Detection and Response) and SIEM protection for endpoints and cloud workloads. Wazuh is free and open source.

## We need to setup Wazuh for file integrity and malware detection.
To achieve this goal, we need to setup and install the following: 
1.	Setting up Wazuh ova file on virtual box.
2.	Accessing the Wazuh dashboard.
3.	Install window 10 on virtual box.
4.	Install Wazuh GUI agent on endpoint.
5.	Install Sysmon on endpoint (windows 10) device.
6.	Integrate Sysmon logs to Wazuh agent.
7.	File integrity (file creation and deletion will be triggered on Wazuh server)
8.	Connecting with total virus to detect malicious payloads.


## Setting up Wazuh server on virtual box:
* Download the Wazuh ova file (https://packages.wazuh.com/4.x/vm/wazuh-4.14.0.ova)
* Google it “How to install ova file on virtual box” if you don’t know.


## Accessing the Wazuh dashboard:
* When the ova file installation finish, login the Wazuh server the username is “wazuh-user” and password is “wazuh”.
*	Type ip a   command and copy the Wazuh server IP address.
*	Open the browser and paste the Wazuh server IP with https.
*	Login to the Wazuh dashboard by using the admin and admin.
*	And enjoy the beautiful Wazuh interface, are we done? no, no there is a lot to do.


## Install Wazuh GUI agent on endpoint:
*	Download Wazuh GUI agent for window 10  (https://packages.wazuh.com/4.x/windows/wazuh-agent-4.14.0-1.msi).
*	Change the manager IP filed with your Wazuh server IP

