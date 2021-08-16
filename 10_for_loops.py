# define list
list = [1, 2, 5, 7, 9]
print('# increment through list using "for item in list:"')
print("list:", list)
for val in list:
    print(val)

print("# use range(1,10) start stop")
for int in range(0, 10):
    print(int)

print("# use range(1,10,2) start stop step")
for int in range(1, 10, 2):
    print(int)

# loop through dicts
person = {'name':'Jamal','age':18,'state':'US'}

# combined for loop condition key:value
print(person.items())
for key, value in person.items():
    print(f'key:{key} value:{value}')

# addition over all numbers in list
numbers = [1,3,5,6,7,9]
result = 0
for number in numbers:
    result += number

print(result)

# break and continue keywords in for loops
for n in [1,2,3,4,5,6,7,8,9]:
    if n < 5:
        continue
    print(n)

for n in [1,2,3,4,5,6,7,8,9]:
    if n == 5:
        break
    print(n)
