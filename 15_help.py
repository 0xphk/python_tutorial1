# fortune favors the prepared mind - socratia

# integrated help() functions
print("list directory objects using 'dir()'\n", dir(), "\n")

print("list objects(functions,types) in module class '__builtins__' using 'dir(__builtins__)'\n", dir(__builtins__), "\n")

print("dir(__builtins__) get type:", type(dir(__builtins__)), "\n__builtins__ get type:", type(__builtins__), "\n")

print("access help for __builtins__.module using 'help(module)' eg. 'help(hex)'\nfor interactive python shells, not for scripts as it uses pager")

print('''get available modules
>>> help('modules')

import a module
>>> import math

verify that module was loaded
>>> dir()

should now list 'math', now list functions in math
>>> dir(math)
['sqrt', 'pi', 'radians'] # just an example

get help for function in math
>>> help(math.radians)

remove imported module, loose access to it though python keeps it somewhere in memory
>>> del math''')
