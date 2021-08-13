# some keywords are reserved not allowed to use
import keyword
from modules import ansicolor

print(ansicolor.fg.red)
print('Reserved keywords that are not allowed to assign to values:')
print(ansicolor.fg.cyan)
print(str(keyword.kwlist).replace('[','',).replace(']','').replace(',','\n').replace(' ',''))
print(ansicolor.reset)

# check if string is reserved keyword
print(keyword.iskeyword('True'))
