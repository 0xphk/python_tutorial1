# lists (arrays)

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
print(primes)
