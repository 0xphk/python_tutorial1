# variables
var1 = 1
#var2 = input("enter 2nd input: ")

# var as specific input data type
#var3 = int(input("enter 3rd input: "))

# store results
result = eval('9 + 2')

# arithmetic
var1 = 22
var2 = 22 + 3
var3 = (22 - 2) * 3

# naming conventions
name = "James"
# underscore preferred over camelCase in PEP8
full_name = "John James"
# camelCase
fullName = "John James"
# uppercase for constants / fixed values
PI = 3.14159
E = 2.1718281828
# can not start with number, so use underscore
_42 = 42

# explicitly define datatype for variable
name: str = "John"
isAdult: bool = True
my_list: list = [1, 2, 3]
decimal: float = 3.14
my_tuple: tuple = (1, 2, 3)
also_a_tuple: tuple = 1, 2, 3.14, '4'
print(type(name))
print(type(isAdult))
print(type(my_list))
print(type(decimal))
print(type(my_tuple))
print(type(also_a_tuple))
