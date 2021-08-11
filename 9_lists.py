# python3 datastructure lists: ordered sequence of objects

"""
[Python3: List vs Tuple vs Set vs Dictionary]

Lists:  for ordered collection of items or sequence of objects,
        indexed, _not_ hashable

Tuples: can be considered as immutable list,
        elements can't be added, removed or replaced after declaration,
        hashable, _not_ indexed

Sets:   unique list w/o order and duplicates,
        fast + union/intersection operations/methods
        not hashable

Dict:   pair of key and values
"""

# list indexes
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
print('\nexample = [1, 2.71828, True, "Alpha", [64, False, [True, 5+0j]]]')
print('''\nelement/   ^  ^        ^     ^         ^   ^       ^     ^
index =    0  1        2     3         4:0 4:1     4:2:0 4:2:1''')

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
