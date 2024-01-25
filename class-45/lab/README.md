# Lab: Pentest Practice 2 of 2

## Overview

The exploitation phase of a pentest is what authorized (FKA: "white hat") hackers are famously known for. In this stage, the pentester utilizes exploit tools and techniques to gain access to target systems. One of these tools is Metasploit.

Today you will perform an attack using a variety of tools and scanners you've studied throughout this class, then document findings in an OSCP-style report.

## Objectives

## Resources

- [class-45-target.ova 7.01 GB Download](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table){:target="_blank"}
  - This is your target system today.
- [OSCP Report Templates Repo](https://github.com/whoisflynn/OSCP-Exam-Report-Template){:target="_blank"}
  - To prepare you for the realities of offensive security reporting, you'll be modeling today's reporting after these OSCP report templates.

## Tasks

- Perform enumeration and exploitation against a target system within the context of a pentest

### Part 1: Staging

Import the class-45-target.ova into Virtualbox. Assign it to NAT Network alongside your Kali Linux VM.

### Part 2: Enumeration

Now that you have imported the target system to Virtualbox, first determine its IP address using an enumeration tool of your choice.

After identifying the target system's IP, you'll need to get an idea of its vulnerabilities by using techniques such as:

- Port scanning
- Vulnerability scanning
- Banner grabbing/service fingerprinting

The usernames for this computer are:

- Administrator
- labuser
- Guest
- user

Based on your findings, determine how you will exploit the target's weaknesses and gain access. Be sure to document the information you uncovered about the target.

### Part 3: Exploitation

It appears this PC has quite a few vulnerabilities; in this stage, you will be performing attack techniques against the target in order to gain access. Techniques you may consider include:

- Brute force authentication
- Shell connectivity
- Privilege escalation

It is important to carefully document your attacks, as you'll need to craft a detailed report for this lab.

### Part 4: Reporting

Document your findings in the OSCP-OS-XXXXX-Lab-Report_Template3.2.docx file, removing any irrelevant templated example data. Upload this file to your Google Drive and link to it in your submission.

For now, don't worry about executive summary and conclusion components. Try to focus on communicating technical findings.

An effective report should be well-organized, free of typos/formatting issues, technically accurate, comprehensive, and generally valuable to a decision maker or stakeholder.

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
