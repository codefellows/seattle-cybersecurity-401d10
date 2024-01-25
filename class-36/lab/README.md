# Lab: XSS with w3af, DVWA

## Overview

XSS allows attackers to execute scripts in the victim’s browser which can hijack user sessions, deface web sites, or redirect the user to malicious sites. Web Security Dojo allows us study XSS in action, then learn how web application vulnerability analysis can be automated using the open source scanning tool, w3af, to detect vulnerabilities like XSS.

> In 2019, 75% of large companies in Europe and North America were hit by XSS attacks. In the same year, XSS attacks comprised a whopping 40% of all cyber attacks! Turns out injecting malicious code into a web site is a favored attack technique by cyber criminals. We'd better learn a thing or two about it! (Source: [Fudzilla](https://www.fudzilla.com/news/50014-cross-site-scripting-xss-were-a-huge-chunk-of-2019-cyber-attacks){:target="_blank"})

## Objectives

- Practice the XSS (Reflected) lab in DVWA
- Use w3af to scan a separate web app for vulnerabilities and document them

## Resources

- [Web Security Dojo VM OVA 5.82 GB Download](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table){:target="_blank"}
- [W3AF](https://w3af.org/){:target="_blank"}
- [Tips for Creating a Strong Vulnerability Assessment Report](https://blog.rsisecurity.com/tips-for-creating-a-strong-vulnerability-assessment-report/){:target="_blank"}

## Tasks

### Part 1: Staging

This lab requires Web Security Dojo OVA.

### Part 2: XSS on DVWA

Login to DVWA as the administrator. For each successful outcome achieved, include the string you typed into the field and a screenshot of the outcome.

- Set DVWA Security to "Low"
- Perform the following XSS (Reflected) exploits:
  - Have the site return your name as a larger font
  - Have the site return your name in a different color
  - Have the site return your name in a popup box
- Set DVWA Security to "Medium"
- Perform the following XSS (Reflected) exploits:
  - Have the site return your name in a popup box

    > Hint: How do you think the site is detecting your script command? Perhaps its defenses are not as "sensitive" as they seem!

  - Have the site return the session cookie in a popup box

    > Hint: How did you get a popup box to appear last time?

If you are pursuing the stretch goal, set DVWA Security to "High" and try to get an alert popup in XSS (Reflected).

### Part 3: Evaluating InsecureWebApp with w3af

In this next part we will scan InsecureWebApp with w3af.

- Launch w3af (GUI version)
- Scan <http://insecure.local:8080/insecure/public/Login.jsp>
- Include a screenshot of the rendered response of the XSS vulnerability as discovered in w3af GUI that is associated with the "Forgot Login" page
- Include a screenshot of the results of the web crawler.

For the discovered XSS vulnerability, document in your submission:

- Name of the vulnerability
- Date of the discovery
- Score based on CVE (Common Vulnerabilities and Exposures) databases
- A detailed description of the vulnerability
- A detailed description of the affected systems
- Details of the process to correct the vulnerability

### Part 4: Reporting

Answer the below prompts in your own words:

- What is XSS, and why is it a security threat?
- What is a session cookie?
- How can a session cookie be abused by an attacker?

### Stretch Goal (Optional Objectives)

- Complete DVWA XSS (Reflected) on "High" security mode.
- Execute the XSS vulnerability on InsecureWebApp.
  - Include in your submission the POC (proof of concept) of the vulnerability for the InsecureWebApp

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
