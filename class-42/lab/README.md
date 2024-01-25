# Lab: Pass the Hash with Mimikatz

## Overview

Mimikatz is a common attack tool that leverages PowerShell code to perform nefarious operations.

Today you will perform a "pass the hash" attack using Mimikatz.

> The name "mimikatz" comes from the French slang "mimi" meaning cute, thus "cute cats."

## Scenario

It's 2am, and you've broken into your client company, Dubious Defenses LLC, as part of the agreed upon full-scope pentest. Your reconnaissance efforts paid off; using tools like social media platforms, drive-by observations, search engines, and Maltego, you were able to determine the most opportune time to break in as well as useful information about all the employees. The rules of engagement are simple: Everything is fair game, just don't disrupt the computer systems. You have gained access to the front receptionist's computer and have managed to establish a foothold on this Windows 7 endpoint as a local administrator, after some social engineering techniques were successfully applied. You want to continue taking over additional systems on the network and establishing administrator controls over them. You notice this network does not have a domain, even though it is mostly Windows OS. There's no employees around at this time of night, so it's going to be all technical skills from here on in. You're wondering what tools and techniques are going to be most effective for taking over these kinds of systems? The accounting computer, "lab2," looks to be a good next target.

## Objectives

- Use the hash of a local user on target1 to gain remote access to target2
- Write a blog post about your experience. It doesn't need to be published... but doing so is recommended.

## Resources

- [Pass the Hash Tutorial](https://cqureacademy.com/blog/identity-theft-protection/pass-hash-attack-tutorial){:target="_blank"}
- [5 Security Writing Tips to Know](https://www.articlecity.com/blog/what-is-content-writing-for-a-security-company-5-security-writing-tips-to-know/){:target="_blank"}

## Tasks

### Part 1: Staging

You will need two target systems for this exercise.

- class-42-target1-win7.ova (credentials are labuser/labuser)
- class-42-target2-win7.ova (credentials are labuser/labuser)

Import both systems into a NAT Network on Virtualbox. Note that class-42-target1-win7 does contain the malware Mimikatz.

### Part 2: Someone Pass the Hash!

- Follow the [Pass the Hash Tutorial](https://cqureacademy.com/blog/identity-theft-protection/pass-hash-attack-tutorial){:target="_blank"} to achieve an administrator shell from target1 to target2.
  - Dump the hashes of local user accounts and identify the hash of the secret NT Administrator user.
  - Using the included tools in C:\Tools, create a local terminal that assumes the identity of the secret NT Administrator user.
  - Abuse your newfound powers to establish a persistent administrator shell to class-42-target2-win7.
- Create a file on target2's desktop. Once you're able to remotely manipulate the target computer as the Administrator user, this portion of the lab is complete.

> At this point in a cyber attack or pentest, you could use Mimikatz to "pivot" from computer to computer, or deliver a custom malware payload that opens up additional opportunities to infiltrate the organization's systems.

- Document the process and include screenshots of key steps taken.

### Part 3: Blogging

Writing blog articles is common practice in the security world. Making useful or interesting contributions to the community is a great way to get your name out there! In this segment, try your hand at writing a blog article about the lab today. Answer the following and include screenshots of key steps taken/challenges faced.

- What is Mimikatz?
- How does the "pass the hash" attack technique work?
- What conditions are required in order for this attack to succeed?
- What steps did you take?
- What challenges did you face in learning this attack technique?
- What are some concluding thoughts on hacking Windows after your learned Mimikatz?

Here's an outline you can follow.

- Introduction
- Synopsis
- Terms
- Tools used
- Attack scenario
- Attack vector
- Conclusion

You don't have to post this on the internet if you don't want to. Do write this in the voice of a security blogger and submit it as your Google Doc today.

## Stretch Goals (Optional Objectives)

Complete the remaining techniques demonstrated in the tutorial.

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
