# Lab: Attacking Juice Shop with Burp Suite

## Overview

Burp Suite is a popular security tool in the web application security space. Complete with a GUI and a paid Professional edition, Burp Suite is often the web security professional's tool of choice.

Today you'll use Burp Suite Community Edition to probe a vulnerable web app, the OWASP Juice Shop.

> "Why the name 'Juice Shop'? In German there is a dedicated word for 'dump,' i.e. a store that sells lousy wares and does not exactly have customer satisfaction as a priority: 'Saftladen.' Reverse-translating this separately as Saft and Laden yields juice and shop in English. That is where the project name comes from." -Björn Kimminich, Pwning OWASP Juice Shop

## Objectives

- Download the `Seclists` word lists
- Complete the lab at [TryHackMe OWASP Juice Shop Room](https://tryhackme.com/room/owaspjuiceshop){:target="_blank"}
  - Do not complete Part 2 Task 7, Persistent XSS and Reflected XSS
- Answer the reporting prompts

## Resources

- [Portswigger: Getting Started with Burp Suite Pro/Community](https://portswigger.net/burp/documentation/desktop/getting-started){:target="_blank"}
  - This is the official documentation from the developers of Burp Suite. The links under "Next steps" will be the most relevant to you, since Burp is already installed on Web Security Dojo.

- [OWASP Juice Shop Project Page](https://owasp.org/www-project-juice-shop/){:target="_blank"}

- [TryHackMe OWASP Juice Shop Room](https://tryhackme.com/room/owaspjuiceshop){:target="_blank"}
  - This lab will cover the following topics; brush up on each as you feel necessary, so you can be prepared for the concepts presented. Always refer to [the latest OWASP Top Ten](https://owasp.org/www-project-top-ten/){:target="_blank"}, not necessarily the links in this TryHackMe room which reference 2017 information. Make sure you can define these concepts before proceeding with the lab.
    - Injection
    - Broken Authentication
    - Sensitive Data Exposure
    - Broken Access Control
    - Cross-Site Scripting XSS
      - DOM XSS
      - Persistent XSS
      - Reflected XSS

  > Accidentally referencing dated information is a rookie mistake, but easy to make! On the upside, sometimes old write-ups can still be useful - so long as you're aware they're not current. Always impose critical thinking skills upon everything you read.

- [TryHackMe Web Fundamentals room](https://tryhackme.com/room/webfundamentals){:target="_blank"}
  - Need a refresher on the fundamentals of how the web works? Check out [TryHackMe's Web Fundamentals room](https://tryhackme.com/room/webfundamentals){:target="_blank"} for a nice breakdown of the following core topics:
    - HTTP request/response cycle
    - Web servers
    - DNS
    - Cookies

- [Daniel Miessler's SecLists GitHub repo](https://github.com/danielmiessler/SecLists){:target="_blank"}

## Tasks

### Part 1: Staging

This lab requires Web Security Dojo VM.

- Juice Shop is manually launched via shell script from the start menu > targets section.
- Access the Juice Shop page to verify it is up.
- Install Git with `sudo apt update` then `sudo apt install git`.
- Git clone [SecLists](https://github.com/danielmiessler/SecLists){:target="_blank"} to your Web Security Dojo.

> If you reboot Web Security Dojo, you'll need to re-launch Juice Shop manually.

### Part 2: TryHackMe Burp Suite Lab

We'll be revisiting TryHackMe's site once again, this time in guiding us on how to use Burp Suite against OWASP Juice Shop.

- Complete the lab at [TryHackMe OWASP Juice Shop Room](https://tryhackme.com/room/owaspjuiceshop){:target="_blank"}. Respond to any questions/prompts here in your submission instead of on the TryHackMe page.

  - Task 1: Open for business!
    - Nothing to do here but to review the primer and move forward into Task 2.

  - Task 2: Let's go on an adventure!
    - What is the administrator's email address?
    - What parameter is used for searching?
    - What show does Jim reference in his review?

  - Task 3: Inject the juice
    - How did you log into Bender's account?
    - How did you log into the administrator's account?

  - Task 4: Who broke my lock?!
    - Brute force the administrator's password. How did you do it?

      > Don't forget, you downloaded SecLists in Part 1.

    - Reset the password. How did you do it?

  - Task 5: AH! Don't look!
    - Access the confidential document. How did you do it?
    - Log into MC SafeSearch's account. How did you do it?
    - Download package.json.bak. How did you get past the error?

  - Task 6: Who's flying this thing?
    - Access the administration page. How did you do it?
    - View another user's shopping basket. How did you do it?
    - Remove all 5-star reviews. How did you accomplish this?

  - Task 7: Where did that come from?
    - This task does not need to be completed, no action required.

  - Task 8: Exploration!
    - View the scoreboard page, no action required.

### Part 3: Reporting

Define the below terms in your own words:

- Injection
- Broken authentication
- Sensitive data exposure
- Broken access control
- XSS

## Stretch Goals (Optional Objectives)

There are 100 Juice Shop challenges that await you. How many can you complete?

- First, discover the carefully hidden 'Score Board' page.

  > There seems to be no link that leads you there! What techniques have you learned this module that would help you find something that's not readily available on a web app?

- Reference Björn Kimminich's book/website, [Pwning OWASP Juice Shop](https://pwning.owasp-juice.shop/){:target="_blank"}, as a "hacking guide" to help you clear more challenges.

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
