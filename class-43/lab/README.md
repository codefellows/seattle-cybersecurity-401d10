# Lab: Traffic Sniffing with Ettercap

## Overview

ARP poisoning can be used in tandem with traffic sniffing to create a man-in-the-middle (MITM) attack on a targeted network.

Today you will perform a man-in-the-middle (MITM) attack using Ettercap, and also get some additional practice with Wireshark.

## Objectives

- Perform offensive network traffic capture using Ettercap
- Decrypt HTTPS packets using Wireshark
- Perform ARP spoofing with the Ettercap command line

## Resources

- [Ettercap Linux Man Page](https://linux.die.net/man/8/ettercap){:target="_blank"}
- [MITM/Wired/ARP Poisoning with Ettercap](https://charlesreid1.com/wiki/Man_in_the_Middle/Wired/ARP_Poisoning_with_Ettercap){:target="_blank"}
- [Pentest Tips: ARP Spoofing](https://pentestfreak.blogspot.com/2013/05/redirect-someone-to-different-website.html){:target="_blank"}

## Tasks

### Part 1: Staging

Deploy two VMs to a NAT Network:

- One Kali VM
- class-42-target2-win7.ova

> Feel free to use a different target VM if you prefer, instead of class-42-target2-win7.ova.

Confirm Ettercap is installed and operational on your Kali machine using the `ettercap --version` command on a terminal window. 
If Ettercap is installed, the command will display the version information. You will see output similar to: `Ettercap v0.8.3 (IPv6) ...` 

- Download [PCAP and log key](https://github.com/pan-unit42/wireshark-tutorial-decrypting-HTTPS-traffic){:target="_blank"} that will be used in Part 3 to your Kali box.

### Part 2: MITM and ARP Cache Poisoning with Ettercap GUI

First let's practice some basics by having Ettercap capture network traffic transmitted between class-42-target2-win7.ova and the internet. To do this, we'll need to perform a simple ARP poisoning attack and then analyze the sniffed packets with Wireshark.

- Set packets to automatically forward from Kali Linux's eth0 interface using the terminal command `sysctl -w net.ipv4.ip_forward=1`.
- In Kali, launch Ettercap and select a sniffing mode.
- Designate your targets.
- On Windows PC, grab a screenshot of the arp cache.
- Perform an ARP poisoning attack to grant Ettercap access to Windows PC.
- On Windows PC, grab a screenshot of the poisoned arp cache. How can you tell it's poisoned?
- Initialize live sniffing in Ettercap, then launch Wireshark. Have Wireshark perform live packet capture on the sniffer interface.
- Perform a ping from the Windows PC to any valid destination IP or URL. If you have successfully performed a MITM attack, you'll see these ping packets.
- Have Wireshark filter down the view to only ICMP packets. Take a screenshot of this successful outcome.
- On the Windows PC navigate a web browser to <http://www.wikidot.com>, then navigate to the "Pricing" link at the top.
- Have Wireshark filter down the view to only HTTP packets. Take a screenshot of the HTTP GET request for the Pricing page.
- Save a PCAP of the captured data to your desktop > Class 43 folder and take a screenshot of the PCAP.

Nice work! You've now achieved foundational proficiency with offensive network traffic capture using Ettercap. That's some useful network traffic you've captured, but what about encrypted HTTPS traffic?

### Part 3: Decrypting HTTPS with Wireshark

Let's get some more Wireshark practice; in this part of the lab, we're going to figure out how to deal with pesky encryption protocols like HTTPS that are getting between us and the precious data we're wanting to capture. Access the [Wireshark Tutorial: Decrypting HTTPS Traffic](https://unit42.paloaltonetworks.com/wireshark-tutorial-decrypting-https-traffic/){:target="_blank"}.

- If you have not done so in staging, download the [PCAP and log key used in this exercise](https://github.com/pan-unit42/wireshark-tutorial-decrypting-HTTPS-traffic){:target="_blank"} to your Kali system.
- Complete the tutorial. Document in your submission today your thoughts and screenshots of key milestones achieved during the tutorial.

Nice work! It looks like there's quite a few approaches we can take to decrypting SSL traffic. Next, let's take a look at some other capabilities of Ettercap.

### Part 4: ARP Spoofing with Ettercap Command Line

Now that you're familiar with the Ettercap GUI, let's delve into a more advanced operation: ARP spoofing. Let's redirect the Windows PC to a different website every time it tries to access apache.org.

- For this part of the lab, use all resources at your disposal to determine how this attack is performed with Ettercap.
- For the website you redirect the Windows user to, try setting up a quick Apache web server on Kali. Alternatively, redirect it to an entirely different website on the internet.
- When the successful outcome is achieved, capture a screenshot of Ettercap's terminal performing the redirect, as well as a screen of the site you sent the unsuspecting user to.

That's some impressive work you did there! I wonder what a cyber criminal could use this for?

### Part 5: Reporting

Answer the discussion prompts below:

- What is ARP poisoning, and how does it work?
- How is ARP spoofing different from DNS poisoning?
- Why might a penetration tester utilize Ettercap on a targeted subnet?
- For what purposes would a malicious attacker use these techniques?

### Stretch Goals (Optional Objectives)

If you want to tie it all together with some more Ettercap exercises, try this stretch goal:

- Use Ettercap to stage a SSL Stripping attack and decrypt the victim's HTTPS traffic.

## Submission Instructions

- Create a new blank Google Doc. Include above assignment submission text and images within this Google Doc.
- Name the document according to your course code and assignment.
  - i.e. `seattle-ops-401d1: Reading 01` or `seattle-ops-401d1: Lab 04`.
- Add your name & date at the top of the Google Doc.
- Share your Google Doc so that "Anyone with the link can view".
- Paste the link to your Google Doc in the discussion field below and share an observation from your experience in this lab.
