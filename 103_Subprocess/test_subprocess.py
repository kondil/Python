#!/usr/bin/env python

# Import the module
import subprocess

cmd = "ls -l | grep test"
ps = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ps.communicate()[0]
print output

ps = subprocess.Popen(('ls', '-l'), stdout=subprocess.PIPE)
output = subprocess.check_output(('grep', 'test'), stdin=ps.stdout)
# ps.wait()

print output
