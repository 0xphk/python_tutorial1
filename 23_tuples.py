# python3 datastructure tuples: can be considered as immutable/hashable list

"""
[Python3: List vs Tuple vs Set vs Dictionary]
https://blog.softhints.com/python-list-vs-tuple-vs-dictionary-vs-set/

Lists:  for ordered collection of items or sequence of objects,
        indexed, _not_ hashable

Tuples: can be considered as immutable list,
        elements can't be added, removed or replaced after declaration,
        hashable, _not_ indexed

Sets:   unique list w/o order and duplicates,
        fast + union/intersection operations/methods,
        not hashable

Dict:   pair of key and values,
        requires lookup by key or value,
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

# operations: count() counts given element/object in tuple, index() gives index of given element/object in tuple
print('print(s1.count(1))')
print(s1.count(1))
print("print(s2.count('jan'))")
print(s2.count('feb'))
print('print(s3.index(0))')
print(s3.index('a'))
