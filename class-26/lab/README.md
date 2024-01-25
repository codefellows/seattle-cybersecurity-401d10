# Lab: Remote Code Execution

## Overview

Threat analysis involves the assessment of adversaries, TTPs, and APTs to better understand threats and therefore mitigate them appropriately. As defenders, we want to ideally simulate a known TTP to best determine mitigation techniques.

Throughout this class, you've developed shell scripts as a form of automation. What if an intruder weaponized such automation and used it against you? Remote Code Execution (RCE) is a software vulnerability that allows a threat actor to execute code on the target computer. As a security practitioner, you'll want to watch out for this and prepare to deal with it in the field.

## Scenario

A major government contractor, Cyberdyne Systems, contacted your Managed Security Services Provider (MSSP) today to help investigate a major security breach that took place only a few days ago. A nation state APT was able to penetrate the company's defenses and wreak havoc on its network before exfiltrating blueprints on a secret project, codenamed T-800. Cyberdyne's internal incident response team saved the relevant logs for further analysis. After signing a NDA, your company agreed to review the provided data logs and implement new detective security controls to remediate the newly-discovered vulnerabilities.

Cyberdyne's Security Director, Miles Dyson, is your point of contact for this project. "We're going to need serious threat modeling on this one," Dyson explained over a Zoom meeting this morning. "We're still piecing together the event logs for you to analyze, so we'll be sending them over to you in batches. Please have a look at this first data set; our IR team reports RCE was used. Let me know what you learn, I've got my top defenders ready to implement remediations once we hear back from you. Good luck!"

## Objectives

- Analyze the provided event logs data set and determine the TTPs used
- Reproduce an attack based on analysis of the incident's log files
- Develop and test a script that protects a Windows system from this RCE technique

## Resources

- [Term2-baseline-lab-v5.zip Download (39 GB)](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table){:target="_blank"}
- [MITRE ATT&CK®](https://attack.mitre.org){:target="_blank"}
- [Mordor Data Set: Empire Invoke PsExec](https://securitydatasets.com/notebooks/atomic/windows/execution/SDWIN-190518210652.html){:target="_blank"}
- [PsExec Artifacts Reference](https://jpcertcc.github.io/ToolAnalysisResultSheet/details/PsExec.htm#Findings){:target="_blank"}
- [Invoke-PsExec for Powershell](https://www.powershelladmin.com/wiki/Invoke-PsExec_for_PowerShell){:target="_blank"}
- [Configure Inputs for the Splunk Add-on for Sysmon](https://docs.splunk.com/Documentation/AddOns/released/MSSysmon/Configureinputs){:target="_blank"}

## Tasks

### Part 1: Staging

This lab utilizes Splunk Enterprise (Trial), Windows Server 2019, and Windows 10. If you'd like to start term 2 with a working baseline threat detection lab environment in VirtualBox, download and import Term2-baseline-lab-v5.zip. You are welcome to use your own VMs instead, but you may need to manually configure things such as VirtualBox network adapters, etc. If you end up using the provided baseline lab, skip to the final two items in the list below. The remaining labs in this module will be instructing you as if you are using the provided lab environment.

- Prepare a Windows 10 VM
- Install Sysmon on Windows 10 VM
- Install Splunk Universal Forwarder on Windows 10 VM to forward logs in real time to Splunk
- On Windows Server, download Invoke-PsExec for Powershell
- Import the Mordor data set, Empire Invoke PsExec, into Splunk for analysis. Note: If you are using the provided Splunk instance, this data set has been pre-loaded for you.
- Before continuing, check that Windows 10 event logs are being forwarded correctly to Splunk.
  - Inspect timestamps. See anything odd? If so, check the time zone setting of the Splunk VM itself and adjust accordingly.
  - After applying the updated time zone, reboot the Splunk VM.
  - Run another query to confirm timestamps are correct.

> ****Note****: If your Splunk instance has an expired enterprise license, you will have daily indexing limits (500MB per day). If you need more than that, follow the Staging Instructions for Splunk (provided above). Otherwise, Splunk free will suffice.

### Part 2: Analysis of a Sample Data Set

In this part of the lab, we will investigate the data set by consulting the PsExec Artifacts Reference as a guide for obtaining critical information from our sample data set. Get ready to practice your SPL querying skills as we comb through a sizeable data set.

- In Windows Server VM, access Splunk at `http://10.0.0.5:8000/en-US/app/launcher/home` and login with `splunkadmin` / `splunkadmin`.
- Perform the search `index="class-26"` to view today's sample data set that has been imported from Mordor Data Sets.
- Identify the three event logs where a network connection was established using powershell.exe
  - Include a screenshot of Splunk indicating the SPL query you used to exclusively display these three logs according to the stated attributes
- What port was used throughout the attack?
- What is the domain prefix and account name that invoked PsExec (e.g. RIVENDELL\Elessar)?
  - When did this invocation take place?
  - What is the location of the executable that this process used?
- What TTPs were used in this attack?
- What part of the kill chain is this?

### Part 3: Simulation of this

Now that we have an idea of what this attack might look like, let's reproduce the remote code execution in our own lab environment. For this simulation we won't be using Empire, but instead be using Invoke-PsExec as a standalone tool from our Windows Server VM. The required components of this activity have been pre-staged for you in the provided baseline lab package. However, feel free to experiment. For example, if `Invoke-PsExec` isn't getting the job done for you, try `PsExec` from Microsoft Sysinternals instead.

- In Windows Server VM, access Splunk at `http://10.0.0.5:8000/en-US/app/launcher/home`
- Check that regular event logs are being correctly forwarded from Win10 by querying `host="DESKTOP-XXXXX"`. Note: Replace the host name with the name of your Win10 VM.
- Check that Sysmon logs are being correctly forwarded from Win10 by querying `source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational"`.
- From Windows Server, access `C:\Users\Administrator\Desktop\ops-cyber-401\Invoke-PsExec.ps1` using PowerShell IDE running as Administrator.
- Execute this script a few times.
- Review your event logs and Sysmon logs. Did this activity generate new logs? Include a screenshot of them.
- Modify the PowerShell script to execute a simple batch script file on the Win10 box instead of a command.
  - Run it a few times.
  - Does this affect the type of event logs coming into Splunk?
  - Does this affect alerting configured to detect this activity?

### Part 4: Reporting

Explain:

- Summarize what you've done and learned today. What are your key takeaways?
- How do Sysmon logs differ from regular event logs?
  - Which type was more useful in this scenario?
- How can a Windows system be vulnerable to RCE?
- Referencing MITRE ATT&CK, what are some other tools and techniques besides `Invoke-PsExec` that can be used to perform RCE?
- What are some countermeasures against RCE?

### Stretch Goals (Optional Objectives)

Preventative measures are important to practice. If time allows, develop and test a PowerShell script that sets configurations on Win10 that protect the system from this PowerShell RCE technique. This should execute against how you replied to the question in Part 4, "What are some countermeasures against RCE?"

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
