#!/usr/bin/env python3
from setuptools import setup

setup(
	name="PowerStager",
	version="0.2.5",
	description="This script creates an executable stager that downloads a selected powershell payload.",
	author="z0noxz",
	author_email="z0noxz@mail.com",
	url="https://github.com/z0noxz/powerstager",
	classifiers=[
		"Development Status :: 0.2.5 - Beta",
		"Intended Audience :: Developers",
		"Intended Audience :: End Users/Desktop",
		"Natural Language :: English",
		"Programming Language :: Python",
		"Topic :: Security :: Exploitation"
	],
	requires=[
		"os",
		"sys",
		"getopt",
		"glob",
		"socket",
		"fcntl",
		"errno",
		"string",
		"re",
		"random",
		"base64",
		"datetime",
		"time",
		"hashlib",
		"readline",
		"signal",
		"urllib",
		"names",
	],
	scripts=["bin/powerstager"],
	packages=["powerstager"]
)