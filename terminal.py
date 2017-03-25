#!/usr/bin/env python2
import getpass, os, sys, random
from subprocess import Popen, PIPE, call

while True:
	command = raw_input("[{}@{} {}] $ ".format(getpass.getuser(), os.uname()[1], os.getcwd()))
	if command.split(" ")[0] == "cd":
		os.chdir(command.split(" ")[1])
	else:
		p = Popen(command.split(" "), stdin=PIPE, stdout=PIPE, stderr=PIPE)
		out, err = p.communicate()
		out = str(out)
		try:
			err = err[0]
		except:
			err = ""
		newout = ""
		newerr = ""
		call(["toilet", out])

