# get installed packages (pacman,yay,pip)
import pkg_resources
import os
from time import sleep
from modules import color, now, term_reset, spinit

# clearing screen using ansi escape sequence works but only cleans the visible parts
# print(color.CLS,color.END)
# better solution to call 'reset' directly
term_reset()

print('>>> collecting package information ...')
sleep(1)

print('>>> getting pip packages ...')
spinit(6)

# collect pip packages using pkg_resources.workingset()
pip_pkg = [(p.project_name, p.version) for p in pkg_resources.working_set]

print('>>> getting pacman/aur packages ...')
spinit(11)

# collect pacman/yay packages using os.popen()
pac_raw = os.popen('pacman -Q').read()  # type str
pac_lst = [pac_raw]
# replace empty value after replacing weird newlines str().replace().replace()
pac_pkg = str(pac_lst).replace("\\n","', '").replace(", ''","")
term_reset()

print(color.CYAN,'\npip pkg:\n',color.END,pip_pkg,sep='')
print(type(pip_pkg))
sleep(1.5)

print(color.DARKCYAN,'\npac_pkg:\n',color.END,pac_pkg,sep='')
# print(color.DARKCYAN,'\npac_pkg:\n',color.END,pac_list,sep='')
print(type(pac_pkg))
sleep(1)

print('\nfinished:',now())

# progress first try using ansi sequences but did not work, though counter worked somehow
# print(str(i),ansi.cmr,' * ',ansi.cmrp,end=' ',sep='\r')
# print(str(i),' >>> ',end=' ',sep='\r')
# for i in range(1,10):
#     print('>>>',end=' ',sep='')
#     print(str(i),'',end='',sep='\r')
#     sleep(0.5)
