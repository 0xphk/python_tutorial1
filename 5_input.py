print('''inputs are strings, use type casting to convert to int or float
    ''')

# inputs
var1 = input("enter 1st input: ")
var2 = input("enter 2nd input: ")
var3 = int(input("enter 3rd input: "))

# get var types
type_var1 = type(var1)
type_var2 = type(var2)
type_var3 = type(var3)

var1
var2
var3

print('input1 was:', var1, '''
input2 was:''', var2, '''
input3 was:''', var3, '''
type var1: ''', type_var1, '''
type var2: ''', type_var2, '''
type var3: ''', type_var3, '''
adding as strings: ''', var1 + var2 + str(var3), '''
adding as integer: ''', int(var1) + int(var2) + var3)
