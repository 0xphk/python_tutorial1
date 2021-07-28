# lists (arrays)

# list indexes
from operator import itemgetter

# define array
list = [1, 2, 5, 7, 9]

# print data type
print(type(list))

# print list
print("list: ", list)

# for loop printing all values
for val in list:
    print(val)

# print index 0 - array item 1
print(list[0], list[4])

# list[0:4] behaves strange, should output items 1 - 5 but outputs items 1 - 4

# slices start stop step
print(list[0:5:1])

print(list[0:5:2])

# use operator.itemgetter() to access multiple list items per index
print(*itemgetter(0, 4) (list))