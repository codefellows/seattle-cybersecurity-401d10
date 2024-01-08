# Lab: Strategic Policy Development

## Overview

Compliance requirements are often a critical business driver for adopting new cybersecurity policies, procedures, and systems. One such compliance standard is System and Organization Controls (SOC) 2. Modern security professionals must be familiar with common industry frameworks and compliance standards, and be prepared to align security operations accordingly.

## Scenario

Your MSSP has recently accepted a new client, a five year-old startup SaaS company called "Initrobe." Initrobe is looking to expand operations and build new partnerships. Increasingly, however, customers are inquiring about Initrobe's security practices (doing their proper due diligence when assessing third-party vendors). The Initrobe CTO is busy growing her engineering and product team, and brought your company in to assess the security landscape, make recommendations, and create and implement Initrobe's security policy and strategy.

Initrobe is a fully remote company with a distributed workforce across the US, and it relies heavily upon cloud IaaS technologies, as well as third-party SaaS and PaaS. There is no IT department (you and the head of HR will coordinate hiring and termination needs).

Initrobe is looking to pursue a SOC 2 Type 2 audit this year. It's now your job to identify vulnerabilities, gaps, and tasks ahead as you tighten up security and prepare for a SOC 2 audit. After reviewing the company’s services and business processes, you’ve gathered the below notes.

Employees

- HRIS - Gusto
- 80 Employees (expected to hire 30 more this year!)
- 25 Contractors (1099)

Domain - Initrobe.com

- Google Workspace is the email and identity agent.
- Employees - Each employee is assigned an email address with the following format firstname.lastname@initrobe.com.
- Contractors - Most contractors are assigned an email address with the following format v-firstname.lastname@initrobe.com but many are using personal emails, some are sharing a single log-in for Initrobe access.

IT Resources

- Fully remote, no on-premise resources
- No hardware inventory
- No software inventory
- No security awareness training
- No mobile device management (MDM) software
- Employees are using a mix of personal computers & company computers (and personal cell phones); primarily macOS fleet, with a few Windows machines, and even fewer Linux boxes (engineering team only).
- Contractors are using personal computers.

Security/data policies in existence:

- Data Security Acknowledgement
- Laptop Lending Form (for employees receiving company laptops)

Among other gaps, there are no formal Incident Response, Business Continuity, and no recovery plans. Furthermore, Initrobe lacks a consolidated or centralized program for management and access or usage audit for remaining ad-hoc assortment of additional vendors and tools (Zoom, Salesforce, Shortcut, Adobe, Microsoft Office) that some people have access and/or admin rights to.

Major tools

- Google Workspace for email and Drive (no password requirements or MFA enforced)
- AWS and Heroku for PaaS needs
- Slack for internal communication
- [Slab](https://slab.com/){:target="_blank"} for internal documents (i.e. Employee Handbook, policies, procedures)
- Google Docs (shared drive) used for additional company documents
- Internal application access (to Initron, the software platform sold by Initrobe), Google Workspace credentials serve as SSO
- Gusto - HRIS (complete with org chart)
- Application (Initrobe's SaaS product, Initron, which is web, iOS, and Android)
- MFA required for platform and source-code access (Heroku, AWS, GitHub)
- Slack notifications to engineering team for critical bugs and vulnerabilities
- [Shortcut project management](https://shortcut.com){:target="_blank"} and ticketing system
- Static & dynamic analysis of applications conducted periodically

SOC 2 compliance will require all computers configured as follows:

- Encrypted hard drive
- Automatic screen lock
- Antivirus installed and scanning
- Automatic OS updates enabled
- Configured to use a password manager application

## Objectives

- Using the provided templates, create the following deliverables:
  - Security Architecture Narrative
    - The narrative should describe the current state of Initrobe's security practices and their liabilities/weaknesses.
  - Information Security Policy
  - Employee Onboarding Procedure
  - Employee Offboarding Procedure
- Create a shell script that automates ONE of the following required SOC 2 configurations on a Windows 10 endpoint.
  - Automatic screen lock
  - Antivirus installed and scanning
  - Automatic OS updates enabled

## Resources

- [SOC 2 Policy Docs Template](https://docs.google.com/document/d/11llh6dLRYYKIKptSA_RX1Siu4D8KvD6_63uNnDsT5N8/edit){:target="_blank"}
- [SOC 2 Compliance Requirements](https://secureframe.com/hub/soc-2/requirements){:target="_blank"}

## Tasks

### Part 1: SOC 2 Deliverables

- Start by carefully reviewing the scenario.
- Access the provided template and create a copy by clicking on File > Make a copy
- Customize the deliverables for today in accordance with the scenario and SOC 2 requirements
  - Security Architecture Narrative
  - Employee Onboarding Procedure
  - Employee Offboarding Procedure
  - Information Security Policy
    - Acceptable Use Policy
    - Disaster Recovery Policy
    - Password Policy
    - Remote Access Policy
    - Workstation Policy

### Part 2: Automating Workstation Configuration

- Select a shell script objective for yourself.
- Write a PowerShell script that achieves the target objective.
  - Test and validate the script works.

## Stretch Goals (Optional Objectives)

- Using the provided templates, also create the following deliverables:
  - Remote Access Policy
  - Server OS Patching Procedure
  - Workstation Management Procedure

- Create a shell script that automates ALL of the following required SOC 2 configurations on a Windows 10 endpoint.
  - Automatic screen lock
  - Antivirus installed and scanning
  - Automatic OS updates enabled

## Submission Instructions

1. Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
1. Name the document according to your course code and assignment.
   - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
1. Add your name & date at the top of the Google Doc.
1. Share your Google Doc so that "Anyone with the link can view".
1. Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
