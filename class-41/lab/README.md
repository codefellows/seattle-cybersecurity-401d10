# Lab: Reconnaissance with Maltego

## Overview

This week, we'll learn about all the stages of a penetration test. The first stage of a penetration test involves reconnaissance.

Today you will use reconnaissance techniques to gather information about your target with Maltego.

> As described in the book [Permanent Record](https://www.amazon.com/Permanent-Record-Edward-Snowden/dp/1250237238/ref=sr_1_2?crid=2SBI75SULSU7M&dchild=1&keywords=permanent+record+edward+snowden&qid=1606880873&sprefix=permanent+record+ed%2Caps%2C201&sr=8-2){:target="_blank"} by Edward Snowden, the internet is like a vast database that maintains histories of our every activity, often unbeknownst to the everyday user. OSINT tools like Maltego can dig up a surprisingly vast amount of information by strictly querying public resources such as DNS servers and public APIs. What you are about to learn is incredibly powerful. Remember we have a duty to live up to the utmost ethical standards, so use this kind of power responsibly!

## Objectives

- Use various Maltego transformations to profile an APT group
- Use various Maltego transformations to profile a company

## Resources

- [Maltego Desktop Documentation](https://docs.maltego.com/support/solutions/articles/15000008831-home-page){:target="_blank"}
- [Maltego Tutorials](https://www.maltego.com/maltego-essentials/){:target="_blank"}
- [Beginner's Guide to Maltego](https://wondersmithrae.medium.com/a-beginners-guide-to-osint-investigation-with-maltego-6b195f7245cc){:target="_blank"}
- [Investigate TA505 Threat Actor Group Using Maltego](https://www.maltego.com/blog/investigate-ta505-threat-actor-group-using-maltego/){:target="_blank"}
- [Mandiant APT41 Threat Report](https://www.mandiant.com/sites/default/files/2022-02/rt-apt41-dual-operation.pdf){:target="_blank"}
- [VirusTotal](https://www.virustotal.com/){:target="_blank"}
- [Hybrid Analysis](https://www.hybrid-analysis.com/){:target="_blank"}

## Tasks

### Part 1: Staging

This lab requires a Kali VM.

If you have not yet done so, create accounts on the following sites in order to use their public APIs:

- [VirusTotal](https://www.virustotal.com/){:target="_blank"}
- [Hybrid Analysis](https://www.hybrid-analysis.com/){:target="_blank"}

> Remember to keep your API keys a secret. A password manager can help you track all this.

### Part 2: Profiling an APT Group

While known for its investigatory powers, Maltego is not strictly an offensive pentesting tool. It can also be used to profile an APT in order for your organization to defend against that APT's TTPs. Resources like [Fire Eye's APT Group List](https://www.fireeye.com/current-threats/apt-groups.html){:target="_blank"} keep track of the most notorious active APTs. While you're more likely to be hit by the everyday phishing scam than an international APT, you'll want to know about these if you end up working for a major well-known enterprise.

- Download the threat report for APT41.
- Generally speaking, what TTPs does APT41 use (e.g. "lateral movement")?
- Identify and discuss at least one signature TTP, hash, or domain used by APT41. How can this knowledge help us protect against APT41?

> "TA505 is a financially motivated threat group that has been active since at least 2014. The group is known for frequently changing malware and driving global trends in criminal malware distribution." -MITRE ATT&CK®

Let's start with investigating the TA505 threat actor group and see what we can do to protect our organization against them.

- Use VirusTotal transformations to identify IP addresses associated with the following domains:
  - Filesharess[.]com
  - Live-en[.]com
  - See-back[.]com
- Include a screenshot of the resulting graph in your submission.
- What can your organization do to defend its networks and users against these known malicious IP addresses? Name at least one specific tool or system you'd use.

Next, let's identify the hashes of known IOCs affiliated with these TA505 domains.

- Use Hybrid Analysis "Query Domain" transformation to identify the hashes and URLs of known IOCs associated with these malicious domains.
- Include this screenshot in your submission.
- Upload a hash to VirusTotal. Did this result in a positive?
- Why or why not might an IOC hash result in a positive on VirusTotal?
- What can your organization do to defend its networks and users against these known malicious artifacts? Name at least one specific tool or system you'd use.

> Be careful not to accidentally browse to these malicious sites.

The Maltego transform, "To Snapshots [Wayback Machine]," can help you trace back the source of the threat.

- Execute To Snapshots [Wayback Machine] Transform against the three malicious domains and include screenshots of the results.
- What are these results?
- What do these results tell us about TA505?

### Part 3: Profiling a Company with Maltego Transforms and Machines

Maltego can be used to research a target organization to learn more about it in advance of an attack, such as a pentest.

- Identify the MX record associated with myspace.com.
- What is an MX record, and how does it affect mail server traffic for the domain, myspace.com?
- If we wanted to disrupt the company's mail server traffic, how could this information be useful to us as an attacker performing recon?

DNS can tell us a lot about a company, if the `WHOIS` records are not obfuscated by the domain owner.

- Identify the email address(es) of the domain's owner.
- Identify the phone number(s) of the domain's owner.
- Where does the domain owner live? Include a screenshot of their Myspace page.
- How can this information be used by an attacker?

The "Machines" in Maltego perform automated investigations for us.

- Use the "Company Stalker" Machine against myspace.com.
- What was returned on the graph?
- Explain how Maltego was able to retrieve this information using the Company Stalker Machine. In other words, what does the Company Stalker Machine do?
- Pull up the Myspace page for one of the email addresses on the graph and include a screenshot of it (keep it work-appropriate!).

Next, let's try to find associated web entities to myspace.com.

- Using Machines, perform a Level 1 Footprint against the domain, myspace.com.
- Include a screenshot of the results. What did this return?
- Identify the mail servers associated with myspace.com. How did Maltego determine this relationship? (Hint: How does the internet work?)
- Identify cities associated with the results. Why is Maltego displaying cities? (Hint: How does IP addressing work?)

### Part 4: Reporting

Using the myspace.com Level 1 Footprint graph, generate a Maltego PDF report, upload it to your Google Drive, then link to it in your submission.

## Stretch Goals (Optional Objectives)

Perform your own investigation against a target APT or company.

- Identify its mail server.
- Identify its domain owner.
- Identify email addresses.

See how much you can find. Just remember to be ethical (and more importantly, legal) about the actions you take using the information gathered.

Discuss your findings in your submission, and include your general thoughts on this tool.

## Submission Instructions

1. Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
1. Name the document according to your course code and assignment.
   - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
1. Add your name & date at the top of the Google Doc.
1. Share your Google Doc so that "Anyone with the link can view".
1. Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
