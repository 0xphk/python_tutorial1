# inspect source of module if lang = python
from modules import color
import inspect

# print color class source
print(color.BOLD,color.DARKCYAN,"inspect sources of imported modules, own class: 'color'",color.END,sep='',end='\n')
try:
    print(inspect.getsource(color))
except OSError:
    print("src not available, not a python module?")
