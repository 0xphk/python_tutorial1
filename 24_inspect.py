# inspect source of module if lang = python
from modules import color
from math import isqrt
import inspect

# print color class source
print(color.BOLD,color.DARKCYAN,"inspect sources of imported modules, own class: 'color'",color.END,sep='',end='\n')
try:
    print(inspect.getsource(color))
except OSError:
    print("src not available, or not a python module?")

# won't work for builtins as most of them a pure C, look at srcs instead
try:
    # print(inspect.getsourcelines(isqrt))
    print('if this returns cpython, it is written in C',inspect.getmodule(isqrt))
except OSError:
    print("src not available, or not a python module?")
