# Solution: Malware Traffic Analysis with Wireshark

2020-11-13 - TRAFFIC ANALYSIS EXERCISE NOTES

ENVIRONMENT:
• LAN segment range: 192.168.200.0/24 (192.168.200.0 thru 192.168.200.255)
• Domain: quiethub.net
• Domain controller: 192.168.200.2 - Quiethub-DC
• LAN segment gateway: 192.168.200.1
• LAN segment broadcast address: 192.168.200.255

EXECUTIVE SUMMARY:
On Thursday, 2020-11-13 at 00:26 UTC, a Windows computer used by Craig Alda was infected with IcedID malware. Several hours later at 09:39 UTC, the infected Windows computer retrieved a Windows executable file for Cobalt Strike malware, and we began seeing Cobalt Strike infection traffic.

DETAILS:
IP address: 192.168.200.8
MAC address: 00:08:02:1c:47:ae (HewlettP_1c:47:ae)
Host name: DESKTOP-JH1UZAE
User account name: craig.alda

INDICATORS OF COMPROMISE (IOCs):
Artifacts found during the forensic investigation:

- C-drive/syuHKYt/vFPKnDV/VSMecyU.dll
- C-drive/Users/craig.alda/AppData/Local/Temp/~2559312.dll
- C-drive/Users/craig.alda/AppData/Local/Temp/tezehu.exe
- C-drive/Users/craig.alda/AppData/Local/Temp/sqlite64.dll
- C-drive/Users/craig.alda/AppData/Local/Temp/~2457218.tmp
- C-drive/Users/craig.alda/AppData/Roaming/Exijopac/uwsida3/baipuyac.png
- C-drive/Users/craig.alda/AppData/Roaming/craig.alda/Maaywuku2.dll
- C-drive/Users/craig.alda/Documents/CV.xlsb
- C-drive/Windows/System32/Tasks/{5FD47D96-5062-7DE3-08DA-938D00A84B6B}

Highlights from the forensic investigation:

SHA256 hash: d9bf5e572d313ddf6f684e93874333e68d493395dc032a1d77c
250018a31548f

- File size: 250,579 bytes
- File location: C:\Users\craig.alda\Documents\CV.xlsb
- File description: Excel spreadsheet with malicious macros

SHA256 hash: ddcf95d87542f2df67aff8941fcd92c71cc704698b00923791e21
285f82bb01a

- File size: 134,656 bytes
- File location: http:\\205.185.113.20\file\3.dll
- File location: C:\syuHKYt\vFPKnDV\VSMecyU.dll
- File description: DLL file retrieved by Excel macros
- Run method: rundll32.exe [filename],DllRegisterServer

SHA256 hash: d25e3a7ed538968e9b78367cd8f8d20f8f55471a1eb27aae277
4272fc8c1c1ce

- File size: 125,952 bytes
- File location: C:\Users\craig.alda\AppData\Local\Temp\~2559312.dll
- File description: DLL file for IcedID
- Run method: regsvr32.exe /s [filename]

SHA256 hash: a09d8c487a135b973af532247d62f46695a53f37add6c66e561
f1c14650290f5

- File size: 125,952 bytes
- Location: C:\Users\craig.alda\AppData\Roaming\craig.alda\Maaywuku2.dll
- File description: Persistent DLL file for IcedID (run through scheduled task)
- Run method: regsvr32.exe /s [filename]

SHA256 hash: 7801b75f545c24cf7fba8e98dc4505d21c1a11fd228d04685f71 4d2a0bef83f0

- File size: 734,720 bytes
- File location: <http://185.141.24.71/download/winnit.exe>
- File location: C:\Users\craig.alda\AppData\Local\Temp\tezehu.exe
- File description: EXE for Cobalt Strike malware
Other files from the forensic investigation:
C:\Users\craig.alda\AppData\Local\Temp\sqlite64.dll
- DLL for SQLite (not malicious, but seen during IcedID infections)
C:\Users\craig.alda\AppData\Local\Temp\~2457218.tmp
- PNG image with encoded data used to create IcedID DLL ~2559312.dll
C:\Users\craig.alda\AppData\Roaming\Exijopac\uwsida3\baipuyac.png
- PNG image with encoded data used to create IcedID DLL Maaywuku2.dll
C:\Windows\System32\Tasks\{5FD47D96-5062-7DE3-08DA-938D00A84B6B}
- Scheduled task for IcedID DLL Maaywuku2.dll

Traffic caused by Excel macro:

- 205.185.113.20 port 80 - 205.185.113.20 - GET /BVd1qKwd
- 205.185.113.20 port 80 - 205.185.113.20 - GET /files/3.dll

Traffic to legitimate domains caused by the initial DLL:

- port 443 - help.twitter.com - HTTPS traffic
- port 443 - support.apple.com - HTTPS traffic
- port 443 - support.oracle.com - HTTPS traffic
- port 443 - www.oracle.com - HTTPS traffic
- port 443 - support.microsoft.com - HTTPS traffic
- port 443 - www.intel.com - HTTPS traffic

Traffic to malicious domains caused by IcedID:

- 143.110.191.95 port 443 - lezasopedrill.cyou - HTTPS traffic
- 198.211.99.24 port 443 - timerdisclaimer.pw - HTTPS traffic
- 198.211.99.24 port 443 - compactmuslimsdeport.pw - HTTPS traffic

Traffic related to Cobalt Strike:

- 185.141.24.71 port 80 - 185.141.24.71 - GET /download/winnit.exe
- 185.141.24.71 port 80 - webintercom76delivery.net - GET /updates.rss
- 185.141.24.71 port 80 - webintercom76delivery.net - POST /submit.php?id=123429392
Saw scanning activity from the infected Window host (DESKTOP-JH1UZAE):
- ICMP ping requests from 198.211.99.0 through 198.211.99.255
- Attempted TCP connections to 198.211.99.4 through 198.211.99.252 over TCP port 445
- ICMP ping requests from 10.0.0.0 through 10.0.0.255
- ICMP ping requests from 192.168.0.0 through 192.168.0.255
