#!/usr/bin/env python
import os

# os.system only gives exit value, no output
return_echo = os.system('/usr/bin/echo test')

ver = 'python --version'
# os.system only gives exit value, no output
return_ver = os.system(ver)

# use os.popen to catch output using os.popen().read()
return_output1 = os.popen('/usr/bin/echo echo_test').read()
return_output2 = os.popen(ver).read()

print('/usr/bin/echo returns: ', return_echo, return_output1, '''
    multiline stuff

    python version is: ''', return_output2)
