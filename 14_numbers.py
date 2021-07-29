# assign value
print("set a = 42")
a = 42

# get type
print("get type", type(a))

# print value of var - only works in plain python shell
a

# print value in script
print("print(a):", a)

# python 2 max int value, python 3 has no attribute maxint
#import sys
#sys.maxint()

# use 'j' suffix to set copmplex numbers
print("set z = 3 + 5.7j")
z = 3 + 5.7j

# get type
print("get type:", type(z))

# print complex number representation
print("print(z):", z)

# print 1st real value?
print("print(z.real):", z.real)

# print 2nd real value? - confusing output
print("print(z.imag):", z.imag)
