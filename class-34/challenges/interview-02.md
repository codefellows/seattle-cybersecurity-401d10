# Interview 02

## Interview Question

- How would you go about performing network traffic analysis?
- What is a TTP, and how can one be used to improve a company's security defenses?
- What's the difference between a data flow diagram and a network topology for the purposes of threat modeling?
- What is a denial of service attack? Please provide an example and what layer of the OSI model your example uses.

## Interviewer Notes

- **Network Traffic Analysis**
- "Network traffic analysis (NTA) is a method of monitoring network availability and activity to identify anomalies, including security and operational issues. Common use cases for NTA include:
  - Collecting a real-time and historical record of what’s happening on your network
  - Detecting malware such as ransomware activity
  - Detecting the use of vulnerable protocols and ciphers
  - Troubleshooting a slow network
  - Improving internal visibility and eliminating blind spots
  - Implementing a solution that can continuously monitor network traffic gives you the insight you need to optimize network performance, minimize your attack surface, enhance security, and improve the management of your resources. However, knowing how to monitor network traffic is not enough. It’s important to also consider the data sources for your network monitoring tool; two of the most common are flow data (acquired from devices like routers) and packet data (from SPAN, mirror ports, and network TAPs)." -[Rapid7](https://www.rapid7.com/fundamentals/network-traffic-analysis/)
  - Tools used in class include Zeek, Snort, and Wireshark.

- **TTPs**
- "ATT&CK stands for adversarial tactics, techniques, and common knowledge. Let’s break this down.
  - Tactics and techniques is a modern way of looking at cyberattacks. Rather than looking at the results of an attack, aka an indicator of compromise (IoC), security analysts should look at the tactics and techniques that indicate an attack is in progress. Tactics are the why of an attack technique. Techniques represent how an adversary achieves a tactical objective by performing an action.
  - Common knowledge is the documented use of tactics and techniques by adversaries. Essentially, common knowledge is the documentation of procedures. Those familiar with cybersecurity may be familiar with the term 'tactics, techniques, and procedures,' or TTP." -[Exabeam](https://www.exabeam.com/information-security/what-is-mitre-attck-an-explainer/)
  - What is the goal of MITRE ATT&CK?
    - "The goal is to create a comprehensive list of known adversary tactics and techniques used during a cyberattack. Open to government, education, and commercial organizations, it should be able to collect a wide, and hopefully exhaustive, range of attack stages and sequences. MITRE ATT&CK is intended to create a standard taxonomy to make communications between organizations more specific.
    - ATT&CK was created out of a need to systematically categorize adversary behavior as part of conducting structured adversary emulation exercises within MITRE’s Fort Meade Experiment research environment." -[Exabeam](https://www.exabeam.com/information-security/what-is-mitre-attck-an-explainer/)

- **Threat Modeling**
  - "Also known as DFD, Data flow diagrams are used to graphically represent the flow of data in a business information system. DFD describes the processes that are involved in a system to transfer data from the input to the file storage and reports generation.
  - Data flow diagrams can be divided into logical and physical. The logical data flow diagram describes flow of data through a system to perform certain functionality of a business. The physical data flow diagram describes the implementation of the logical data flow." -[Visual Paradigm](https://www.visual-paradigm.com/guide/data-flow-diagram/what-is-data-flow-diagram/)
  - "Network topology is used to describe the physical and logical structure of a network. It maps the way different nodes on a network--including switches and routers--are placed and interconnected, as well as how data flows." -[Cisco](https://www.cisco.com/c/en/us/solutions/automation/network-topology.html)

- **DoS**
- "A denial-of-service (DoS) attack occurs when legitimate users are unable to access information systems, devices, or other network resources due to the actions of a malicious cyber threat actor. Services affected may include email, websites, online accounts (e.g., banking), or other services that rely on the affected computer or network. A denial-of-service condition is accomplished by flooding the targeted host or network with traffic until the target cannot respond or simply crashes, preventing access for legitimate users. DoS attacks can cost an organization both time and money while their resources and services are inaccessible.
- There are many different methods for carrying out a DoS attack. The most common method of attack occurs when an attacker floods a network server with traffic. In this type of DoS attack, the attacker sends several requests to the target server, overloading it with traffic. These service requests are illegitimate and have fabricated return addresses, which mislead the server when it tries to authenticate the requestor. As the junk requests are processed constantly, the server is overwhelmed, which causes a DoS condition to legitimate requestors.
- In a Smurf Attack, the attacker sends Internet Control Message Protocol broadcast packets to a number of hosts with a spoofed source Internet Protocol (IP) address that belongs to the target machine. The recipients of these spoofed packets will then respond, and the targeted host will be flooded with those responses.
- A SYN flood occurs when an attacker sends a request to connect to the target server but does not complete the connection through what is known as a three-way handshake—a method used in a Transmission Control Protocol (TCP)/IP network to create a connection between a local host/client and server. The incomplete handshake leaves the connected port in an occupied status and unavailable for further requests. An attacker will continue to send requests, saturating all open ports, so that legitimate users cannot connect." -[CISA](https://us-cert.cisa.gov/ncas/tips/ST04-015)
