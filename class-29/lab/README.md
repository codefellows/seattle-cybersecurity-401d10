# Lab: Modeling a Web Application

## Overview

The STRIDE model developed by Microsoft is a popular means of identifying computer threats, providing six major categories that most threats fall into. These threats can then be modeled into data flow diagrams (DFDs) to thoroughly visualize all movements of data in our system, granting a high level overview of processes, data stores, data flows, and trust boundaries. By utilizing threat models, protectors of essential computer systems can evaluate security threats in a systematic and structured fashion, allowing for more strategic and calculated formulation of defensive countermeasures.

Today you will perform threat modeling using the [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started){:target="_blank"}.

## Scenario

This morning, Director Dyson addressed the final requirements for the project. "It has been a pleasure working with your team. We've made great progress in shoring up our defenses, and I have one last request to make of you. Our internal security teams would like to continue exploring the possibility of attack, and proactively implement defenses tailored to our environment. We suspect that the intruder was able to exploit a flaw in our public-facing web application, Genisys. Would you take a look at our processes and construct a threat model? This would be of long-term value as we make important changes to the way our systems interact with one another. I'll forward you the details on our processes."

A few hours later, Director Dyson forwarded you the specifications of their public-facing web application, Genisys. Genisys is a cloud HRIS that employees can access from home to view paystubs or request time off. Here are the key highlights you wrote down as you read through the spec sheet:

- Employee records are saved as entries in the Microsoft SQL Server database, which resides on a Windows Server 2019 instance on AWS.
- The Windows Server 2019 instance is deployed to a private subnet (10.10.1.0/28) of the VPC, 10.10.0.0/24.
- SQL transactions are performed between the Windows Server 2019 instance and the Genisys web app, which is hosted on an Ubuntu Server 20.10 instance in the public subnet (10.10.2.0/28) of the VPC. An internet gateway with the public IPv4 address of 76.233.251.6 brokers traffic to the outside world.
- An AWS Web Application Firewall (WAF) is deployed to protect Genisys from common exploits. The WAF keeps a close eye on all traffic between external users and Genisys. HTTPS traffic from external users is transmitted to the WAF first, which then forwards the traffic via HTTP to Genisys. Conversely, outbound traffic takes the form of HTTP to the WAF, which forwards it as HTTPS to external users.
- The internet boundary resides between the WAF and Genisys.
- Because the public subnet is treated as a DMZ, a local DMZ boundary exists between Genisys and the private subnet.
- The private subnet is directly accessible via AWS VPN for power users like Cyberdyne's resident DBA, Peter Silberman, who works remotely and interacts with the database via SQL Server Management Studio (SSMS) client software installed on his home desktop computer. By activating his OpenVPN client software and authenticating into AWS VPN, the DBA is able to see Windows Server 2019 instance as if it were on his network as an IP address. His business is encrypted between his desktop and the database.
- The Windows Server 2019 instance is accessible to Systems Administrator Tarissa Dyson by way of Teamviewer, a remote desktop application installed on the instance itself. An Elastic IPv4 address of 247.83.118.139 is assigned to the Windows Server 2019 instance, with a security group that allows inbound traffic on network ports 80 and 5938 for Teamviewer requests.

## Objectives

- Use the Microsoft Threat Modeling Tool to construct a DFD based on the scenario above
  - Clearly indicate all key assets, processes, and trust boundaries
- Generate a STRIDE threat model; after all, what could go wrong?

## Resources

- [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started){:target="_blank"}
- [Microsoft Threat Modeling Security Fundamentals](https://docs.microsoft.com/en-us/learn/paths/tm-threat-modeling-fundamentals/){:target="_blank"}
- [Template: Web Application Threat Model](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff648866(v=pandp.10)?redirectedfrom=MSDN){:target="_blank"}
- [Template Sample: Web Application Threat Model](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff649779(v=pandp.10)?redirectedfrom=MSDN){:target="_blank"}

## Tasks

### Part 1: Staging your Toolkit

You will need [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started){:target="_blank"} for today's lab.

- Download and install [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started){:target="_blank"}

### Part 2: Threat Modeling

- Generate a threat model DFD using [Microsoft Threat Modeling Tool](https://docs.microsoft.com/en-us/azure/security/develop/threat-modeling-tool-getting-started){:target="_blank"}. Elements of your DFD will include:
  - Web application server
  - WAF
  - Data store
  - All trust boundaries
  - User/threat actor
  - Tools used by threat actor
  - Systems Administrator
  - DBA
  - All data flows and processes involved in the normal utilization and maintenance of your web app, including:
    - End user access
    - Administrator access
  - All security mechanisms in place such as encryption protocols
    - Example: A web app may support OAuth for Facebook and Google.

### Part 3: Communicate Findings

- Referencing the example in [Template Sample: Web Application Threat Model](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff649779(v=pandp.10)?redirectedfrom=MSDN){:target="_blank"}, compose in your submission a full web application threat modeling report. Use DREAD to guide your thought process on what threats are present.
  - Utilize [Template: Web Application Threat Model](https://docs.microsoft.com/en-us/previous-versions/msp-n-p/ff648866(v=pandp.10)?redirectedfrom=MSDN){:target="_blank"}

When finished, submit both your Web Application Threat Model and DFD in a single Google Doc as indicated below.

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
