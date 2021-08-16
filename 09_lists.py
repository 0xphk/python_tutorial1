# python3 datastructure lists: ordered sequence of objects

"""
[Python3: List vs Tuple vs Set vs Dictionary]
https://blog.softhints.com/python-list-vs-tuple-vs-dictionary-vs-set/

Lists:  for ordered collection of items or sequence of objects, var = [1, 2, '3']
[]      indexed, _not_ hashable

Tuples: can be considered as immutable list, var = (1, '2', 3.14) or var = 1, '2', 3.14
()      elements can't be added, removed or replaced after declaration,
        only index() and count() method,
        immutable, ordered, hashable, _not_ indexed

Sets:   unique list w/o order and duplicates, var = set()
set()   fast + union/intersection operations/methods,
        not hashable

Dict:   pair of key and values, var = {'key1':value,...}
{}      requires lookup by key or value,
        every key requires a value,
        values can be added, removed or modified values of dictionaries,
        indexed keys, no ordering
"""

# list indexes
from modules import term_reset
from operator import itemgetter

# define array
list = [1, 2, 5, 7, 9]

# print data type
print(type(list))

# for loop printing all values
# for val in list:
#    print(val)

# print list
print('whole list: ', list)

# print index 0, index 4
print(list[0], list[4])

# list[0:4] behaves strange, should output items 1 - 5 but outputs items 1 - 4
# is last index (index += 1)? confusing
print(list[0:5:1])

# slices start stop step
print('using slices, id 0 to id 5 steps 1: print(list[0:5:1])')
print(list[0:4:1])
print('using slices, id 0 to id 5 steps 2', print(list[0:5:2]))
print(list[0:4:2])

# use operator.itemgetter() to access multiple list items per index
print('itemgetter()', *itemgetter(0, 4)(list))

# socratia lists [https://www.youtube.com/watch?v=ohCDWZgNIU0&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=14]

# primes = list() # maybe python2, does not work in python3
# define emtpy list
primes = []
print(primes)
print(type(primes))

# add elements to list, keep ORDER
primes = [2, 3, 5, 7, 11, 13]
print(primes)
primes.append(17)
primes.append(19)
print(primes)

# slicing starts w/ beginning value is INCLUDED, ending value is NOT
# this explains why last element in range is element-1, STILL CONFUSING
# print range from list using index x:y [index starts from 0]
print('whole prime list', primes)
# get last element (-1) create new list, display index 0 which is the only index at this time
print(primes[-1:])
# return type list
print(type(primes[-1:]))
# get last element (-1) create new list, display element index 0 which is the only index at this time, return as int
print(primes[-1:][0])
# returns type integer
print(type(primes[-1:][0]))
# get last element in list

# lists can contain different data types like sets, even contain other lists
example = [1, 2.71828, True, "Alpha", [64, False, [True, 5+0j]]]
print(example)
print('\nexample = [1, 2.71828, True, "Alpha", [64, False, [True, 5+0j]]]')
print('''\nelement/   ^  ^        ^     ^         ^   ^       ^     ^
index =    0  1        2     3         4:0 4:1     4:2:0 4:2:1''')
print('\naccess list elements inside list elements: print(example[4][2][1])')
print(example[4][2][1])

# print element 4 which is a list, print element 0 from that list
print('\nprint inside element[4] the element[0] or index[0]:\nprint(example[4][0]) =', example[4][0])
print('print inside element[4] the next_list element[2] and index[1]:\nprint(example[4][2][1]) =', example[4][2][1])

# concatenation of lists
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
print('numbers = [1, 2, 3]')
print("letters = ['a', 'b', 'c']")
print('numbers + letters')
print(numbers + letters)
print('letters + numbers')
print(letters + numbers)
print('reverse order in lists')
numbers.reverse()
letters.reverse()
print('concatenate reversed lists')
print(numbers + letters)

# mosh - list ranges still confusing
print()
list = ['John','Bob','Mary','Jane','Mosh']
print(list)
# again, range does not include the last element
# range starts with index, but 2nd attr is not an index, it is more of a count value?
# so basically start at index[0] and count index+next_x_elements until count reached [0:5]?
# index starts at 0, count starts at index 0 but starting with 1
print(list[0:4])
# same as above, added step attr
print(list[0:4:1])
# positive index from start 0 to end+1, negative index from end -1 to start -4
# weird behavior, looks like you can not get a whole list as range
# -1 prints 'mosh' 0 prints 'John' range [0:-1] excludes last element too
print(list[0:-1:1])
# print list[0:4] does not alter original list but creates an intermediate list on the fly

# list methods append, insert after index
numbers = [1,2,3,4,5]
print(numbers)
# append 6
numbers.append(6)
print(numbers)
# insert at index 0 int 0
numbers.insert(0, 0)
print(numbers)
# boolean expression - return bool if 1 is in list | 10 is in list
print(1 in numbers)
print(10 in numbers)
# get number of elements in list as length in numbers
print(len(numbers))
print('iterate')
# iterate through elements, print
for element in numbers:
    print('for element in var',element)
# same but not storing list as var
for element in range(5):
    print('for range(5)',element)

# same result but more complex
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# range object, 0 to 5 but exclude 5
numbers = range(5)
print(range)
term_reset(30)
print(numbers)
