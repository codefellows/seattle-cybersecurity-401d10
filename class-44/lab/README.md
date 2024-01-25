# Lab: Pentest Practice 1 of 2

## Overview

The exploitation phase of a pentest is what authorized (FKA: "white hat") hackers are famously known for. In this stage, the pentester utilizes exploit tools and techniques to gain access to target systems. One of these tools is Metasploit.

Today you will perform an attack using a variety of tools and scanners you've studied throughout this class, then document findings in an OSCP-style report.

## Objectives

- Perform enumeration and exploitation against a target system within the context of a pentest

## Resources

- [class-44-target.ova 855 MB Download](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table){:target="_blank"}
  - This is your target system today.

- [Kali VM Download](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table){:target="_blank"}
  - Load up this Kali VM and use these labs to prepare yourself for the final project. Usage of this VM is optional but recommended.

- [OSCP Report Templates Repo](https://github.com/whoisflynn/OSCP-Exam-Report-Template){:target="_blank"}
  - To prepare you for the realities of offensive security reporting, you'll be modeling today's reporting after these OSCP report templates.

- [Metasploitable 2 Exploitability Guide](https://docs.rapid7.com/metasploit/metasploitable-2-exploitability-guide){:target="_blank"}
- [Attack Metasploitable 2 Using Metapsloit](https://blog.securelayer7.net/attacking-metasploitable-2-using-metasploit/){:target="_blank"}
  - Reference these guides if you get stuck, or would like a more guided experience in lab today. Keep in mind that such write-ups, while useful for learning offensive tactics, will not be provided during the final project.

## Tasks

### Part 1: Staging

First, import the class-44-target.ova into Virtualbox. Assign it to NAT Network alongside your Kali Linux VM.

Next, import a Kali VM into Virtualbox. Load all pentest scripts into this VM. Assign it to a NAT Network alongside your target box. You may opt to use your own existing Kali Linux instead, if you prefer.

If you have access to any licensed software such as Burp Suite Enterprise or Metasploit Pro, feel free to use it today. However, this lab can be completed with the Kali Linux VM.

### Part 2: Enumeration

Now that you have imported the target system to Virtualbox, first determine its IP address using an enumeration tool of your choice.

After identifying the target system's IP, you'll need to get an idea of its vulnerabilities by using techniques such as:

- Port scanning
- Vulnerability scanning
- Banner grabbing/service fingerprinting

Based on your findings, determine how you will exploit the target's weaknesses and gain access. Be sure to document the information you uncovered about the target.

### Part 3: Exploitation

It appears this PC has quite a few vulnerabilities; in this stage, you will be performing attack techniques against the target in order to gain access. Techniques you may consider include:

- Brute force authentication
- Shell connectivity
- Privilege escalation

It is important to carefully document your attacks, as you'll need to craft a detailed report for this lab.

### Part 4: Reporting

Document your findings in the OSCP-OS-XXXXX-Lab-Report_Template3.2.docx file, removing any irrelevant templated example data. Upload this file to your Google Drive and link to it in your submission.

An effective report should be well-organized, free of typos/formatting issues, technically accurate, comprehensive, and generally valuable to a decision maker or stakeholder.

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
