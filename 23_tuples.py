# python3 datastructure tuples: can be considered as immutable/hashable list

"""
[Python3: List vs Tuple vs Set vs Dictionary]
https://blog.softhints.com/python-list-vs-tuple-vs-dictionary-vs-set/

Lists:  for ordered collection of items or sequence of objects, var = [1, 2, '3']
[]      methods: append,count,insert,reverse,clear,extend,pop,sort,copy,index,remove
        indexed, _not_ hashable

Tuples: can be considered as immutable list, var = (1, '2', 3.14) or var = 1, '2', 3.14
()      elements can't be added, removed or replaced after declaration,
        only index() and count() method,
        immutable, ordered, hashable, _not_ indexed

Sets:   unique list w/o order and duplicates, var = set()
set()   fast + union/intersection/diff operations/methods,
        not hashable

Dict:   pair of key and values, var = {'key1':value,...}
{}      requires lookup by key or value,
        every key requires a value,
        values can be added, removed or modified values of dictionaries,
        indexed keys, no ordering
"""

# tuple declaration
s1 = (1, 2, 3, 4, 1)
s2 = ('jan','feb','mar','apr','may','june','july','aug','sep','oct','dec','jan')
s3 = ('a', 0, 3.14)

print(s1)
print(type(s1))
print(s2)
print(type(s2))
print(s3)
print(type(s3))

# operations: count() counts given element/object in tuple, index() gives index of 1st element/object in tuple
print('print(s1.count(1))')
print(s1.count(1))
print("print(s2.count('jan'))")
print(s2.count('feb'))
# get index of fist match
print('print(s3.index(0))')
print(s3.index('a'))
