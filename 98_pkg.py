# get installed packages (pacman,yay,pip)
import pkg_resources
import os
from time import sleep
from modules import color, now, term_reset, spinit

# collect pacman/yay packages
pac_pkg = os.popen('pacman -Q').read()

# clearing screen using ansi escape sequence works but only cleans the visible parts
# print(color.CLS,color.END)

# better solution to call 'reset' directly
term_reset()

print('>>> collecting package information ...')
sleep(1)

# print('getting pip packages',end=' ',sep=' ')
print('>>> getting pip packages ...')

# call spinning cursor
spinit()

# create list using pkg_resources
pip_pkg = [(p.project_name, p.version) for p in pkg_resources.working_set]
print('>>> getting pacman/aur packages ...')
spinit()
term_reset()

print(color.CYAN,'\npip pkg:\n',color.END,pip_pkg,sep='')
sleep(1)
print(color.DARKCYAN,'\npac_pkg:\n',color.END,pac_pkg,sep='')

print('finished:',now())

# progress first try using ansi sequences but did not work, though counter worked somehow
# print(str(i),ansi.cmr,' * ',ansi.cmrp,end=' ',sep='\r')
# print(str(i),' >>> ',end=' ',sep='\r')
# for i in range(1,10):
#     print('>>>',end=' ',sep='')
#     print(str(i),'',end='',sep='\r')
#     sleep(0.5)
