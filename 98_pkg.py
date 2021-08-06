# get installed packages (pacman,yay,pip)
import pkg_resources
import os
import time
from modules import color, now, term_reset

# collect pkgs
pip_pkg = [(p.project_name, p.version) for p in pkg_resources.working_set]
pac_pkg = os.popen('pacman -Q').read()

# clearing screen using ansi escape sequence partially works
# print(color.CLS,color.END)

# better solution to call 'reset' directly
term_reset()

print(color.CYAN,'\npip pkg:\n',color.END,pip_pkg,sep='')
time.sleep(1)
print(color.DARKCYAN,'\npac_pkg:\n',color.END,pac_pkg,sep='')

print('finished:',now())
