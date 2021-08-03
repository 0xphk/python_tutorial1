# define set (note the missing colon on end of line)
example = set()
# print directory (should list example)
print(dir(example))

# print interactive help for add function/method
# print(help(example.add))

# print type
print(example.add)

# add some elements w/ different data types to example set (int, bool, float, string)
example.add(42)
# if the same element is added multiple times, it gets ignored after 1st add
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

# in sets, element order DOES NOT MATTER, in lists and tuples order DOES MATTER!
print(example)
# print number of elements in set using len()
print('Elements =', len(example))

# remove elements from sets using remove() function/method
# remove non-existing element raises KeyError:
print(example.remove)
example.remove(42)
# example.add(42)
print(example)
print('Elements =', len(example))

# remove/discard elements using discard() function/method
# if one wants notfication about removing non-existing elements from set() use remove, otherwise use discard
print(example.discard)
example.discard(43)
print(example)

# define elements during creation of set
example2 = set([23, True, 2.71828, "Helium"])
example2.discard(True)
print(example2)
example2.add(True)
print(example2)

# clear all elements
example2.clear()
print(example2)
print(type(example2))

# union of different sets intersection = AUB, outer = A/\B
# set some integers
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
# dividable by 1 or itself only
primes = set([2, 3, 5, 7])
# numbers that can be factored
composites = set([4, 6, 8, 9, 10])

# combine output of different sets using union() method (class method_descriptor)
print('set.union()')
print(set.union)
print(type(set.union))
# print odds and evens as new set
print(odds.union(evens))
# works the same if input is reversed
print(evens.union(odds))

# print intersection of odds and primes
print(odds.intersection(primes))
# print differences of evens and primes
print(evens.difference(primes))
# print intersection of primes and odds
print(primes.intersection(evens))
# emtpy intersection of evens and odds
print(evens.intersection(odds))
# print diff of evens and odds and vice versa
print(evens.difference(odds))
print(odds.difference(evens))

# combine primes with composites, note 1 is missing as it is not a composite or prime
print(primes.union(composites))

# check for elements in sets using _in_ keyword 'element' in 'set_name' return bool
print('is number 2 a prime?', 2 in primes)
print('is number 7 a prime?', 7 in primes)
print('is number 6 not a prime?', 6 not in primes)
