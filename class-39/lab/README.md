# Lab: SQLi with Burp Suite, Web Goat

## Overview

SQL injection is a prominent attack technique. By exploiting known deficiencies in web app code, an attacker can compromise the confidentiality of the attached database and manipulate the input to extract desirable information such as user names and passwords.

Today you will study SQL injection in action and complete various tasks and challenges using Burp Suite in Portswigger and OWASP Web Goat.

## Objectives

- Access Web Goat and complete the basic SQL lab
- Access [Portswigger Academy](https://portswigger.net/web-security/all-labs){:target="_blank"} and complete at least three of the SQL labs
- Answer the reporting prompts

## Resources

- [Portswigger Academy](https://portswigger.net/web-security/all-labs){:target="_blank"}

## Tasks

### Part 1: Staging

This lab requires Web Security Dojo VM with an internet connection (NAT mode is recommended).

### Part 2: OWASP Web Goat

OWASP Web Goat comes preinstalled on Web Security Dojo.

- Web Goat does not start automatically in Security Dojo. You'll need to start it manually from command line. Open a terminal in Security Dojo and enter `sudo bash /home/dojo/targets/bin/webgoat-ng-Start.sh` to initialize Web Goat.
- In Firefox browse to `http://webgoat.local:8081/WebGoat/` and login as `guest`, password `guest`. If you encounter an "Unable to connect" error in Firefox, it means either Web Goat did not initialize correctly or the address was incorrectly typed.
- On the left pane you'll see various topics to explore (if you do not, Web Goat did not initialize correctly and you'll need to `sudo reboot now` and try the above launch steps again). Navigate to Injection Flaws and complete the following sections:
  - String SQL Injection
  - LAB: SQL Injection
    - Stage 1: String SQL Injection
    - Stage 3: Numeric SQL Injection
- Turn on your proxy in your browser, and make sure `Intercept is on` in Burp Suite.
- If you get stuck, click "Show Hints" and click the arrow button repeatedly to view additional hints.
- Summarize what you did and learned in your submission.

### Part 3: Portswigger

Portswigger is the company that created Burp Suite. They also happen to have a free training resource for web security students.

- Access [Portswigger Academy](https://portswigger.net/web-security/all-labs){:target="_blank"} and complete at least three of the SQL labs.
- Answer any questions/prompts in your submission doc, as well as explain the concept and what you did in each lab in detail.
- Clearly indicate why and how your solution works for the lab.

### Part 4: Reporting

Answer the below questions in your own words:

- What is SQL injection?
- How is SQL injection detected?
- How can a web app developer defend against SQL injection?

## Stretch Goals (Optional Objectives)

Complete additional Web Goat and/or Portswigger labs.

## Submission Instructions

1. Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
1. Name the document according to your course code and assignment.
   - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
1. Add your name & date at the top of the Google Doc.
1. Share your Google Doc so that "Anyone with the link can view".
1. Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
