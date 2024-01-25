# Lab: Threat Hunting with YARA

## Overview

Defenders should be proficient with VirusTotal's YARA engine, a powerful platform for devising custom signature-based detection rules for malware. Anti-malware applications like ClamAV utilize the YARA engine. By putting these tools together, we can achieve new heights in security automation.

Today you will write your first YARA rule, then feed it into ClamAV to enhance its detection capabilities.

## Resources

- [FLARE VM OVA V2 20.6 GB Download](https://codefellows.github.io/ops-401-cybersecurity-guide/curriculum/#downloads-table){:target="_blank"}
- [FLARE VM GitHub Repo](https://github.com/fireeye/flare-vm){:target="_blank"}
- [Cmder](https://cmder.net/){:target="_blank"}
- [ClamAV](http://www.clamav.net/){:target="_blank"}
- [Using ClamAV On Windows](https://blog.didierstevens.com/2017/08/24/quickpost-using-clamav-on-windows/){:target="_blank"}
- [Hunting with YARA rules and ClamAV](https://blog.nviso.eu/2017/02/14/hunting-with-yara-rules-and-clamav/){:target="_blank"}

## Tasks

### Part 1: Staging

- Download and import the Flare VM OVA.
- Set the network adapter to NAT Network.
- Login as `labuser / labuser`.

> FLARE (FireEye Labs Advanced Reverse Engineering) VM is a fully customizable, Windows-based security distribution for malware analysis, incident response, penetration testing, and more. This week we will be using it primarily as a malware analysis lab environment. You can install this distribution yourself using the [FLARE VM GitHub repo](https://github.com/fireeye/flare-vm), just be aware this is a very lengthy install process that takes several hours.

For this lab, try using the `Cmder` console emulator. Similar to GIT Bash, this lets you navigate through Windows using Linux commands.

### Part 2: My First YARA Rule

YARA rules can be customized to the needs of your detection systems. Let's write a simple detection rule that looks for a specific string in a text file, then execute the rule by directly calling YARA from the command line.

> TIP: To succeed with YARA rules, familiarize yourself with YARA rule syntax. What do the components of a rule file mean when executed? Use the included example rules to help you learn this.

- Access the "yara tools" folder on the desktop. This shortcut will take you to the directory where `yara64.exe` is installed. You'll need to call `yara64.exe` from command line to use it.
- Create a text file containing a string of your choosing.
- Create a YARA rule that tests whether the target file contains the string of your choosing.
- Include comments in your YARA rule.
- Execute the YARA rule against the target file.
- Include a screenshot of the YARA rule and its output.
- Explain whether the rule tested positive or negative. How can you tell?
- Create a file that does not contain your string. Run your rule against it to generate a negative. Note the difference in output.

### Part 3: Customizing ClamAV with YARA Rules

ClamAV is an open source antivirus that supports YARA rules. Let's test this out by having ClamAV scan a file using our custom YARA rule.

> TIP: Take it slow in this part of the lab and review the provided resources. ClamAV is open source; that means there's more configuration involved than a commercial software application would require. Remember what configuring Snort was like?

- Run Fresh Clam to pull the latest virus signatures database into ClamAV's database directory. You may need to edit the configuration files in ClamAV directory to facilitate the process.
- Practice running ClamAV to perform a scan against the `eicar.com` file in the ClamAV directory.
- Include a screenshot of the positive detection.

Now that we've got ClamAV up and running like a normal antivirus solution, let's get to the fun part: Customizing ClamAV's detection algorithm by writing our own YARA rule and adding it to ClamAV's logic.

- Use ClamAV to scan your target text file from Part 2 using the rule you created in Part 2. Do this by instructing ClamAV to use your YARA rule instead of its signature database. Include a screenshot and explanation of how you achieved this.
- Next, instruct ClamAV to scan the target text file from Part 2 using both the rule we created and ClamAV's signature database. Include a screenshot and explanation of how you achieved this.

PE files contain the string "MZ". Let's create a rule that determines whether the target is a PE file.

- Create a new YARA rule named "is_pe_file_clamav_1.yara".
- Write the rule to look for the string "MZ" in its target.
- Test the rule using ClamAV against a PE file and a non-PE file. Include screenshots and discussion.

### Part 4: Reporting

That was just the beginning of what YARA rules can detect. There's plenty more you can do with the powerful YARA engine and software that can use it. The one-two combination of YARA and ClamAV means you now have access to an extensible anti-malware toolkit for any environment.

> "Extensibility is a measurement of a piece of technology’s capacity to append additional elements and features to its existing structure. A software program, for example, is considered extensible when its operations may be augmented with add-ons and plugins. Extensible programming languages have the ability to define new features and introduce new functionality within them." -Techopedia

Answer the below prompts to the best of your ability:

- What else can YARA detect?
- What if you don't have a single string to search for in the target?
- How would you explain ClamAV's "file decomposition" feature?

## Stretch Goals (Optional Objectives)

- Write and test an additional YARA rule that scans an email file for specific data, such as a subject line string.
- Have ClamAV use both the rule and its signature database to perform the scan against an email file.
- Discuss your results.

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
