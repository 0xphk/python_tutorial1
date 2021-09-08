# python2+3 - int
print("set a = 42")
a = 42
print("set b = 23")
b = 23
print("set c = 23.0 # set as float not int")
c = 23.0

# get type
print("get type a:", type(a), "\nget type b:", type(b), "\nget type c:", type(c))

# print value of var - only works in plain python shell
a
b
c

# print value in script
print("print(a):", a, "\nprint(b):", b, "\nprint(c):", c)
print()

# python2 - maxint
# max int value, python 3 has no attribute maxint
#import sys
#sys.maxint()

# python2 only ### use 'L' suffix for long numbers
#print("set y = 1L")
#y = 1L
#print("get type:", type(y))

# square / squareroot syntax
print('''calculate square of x 'x² / x^2' using x ** 2

# using x ** n (x^n) square n = 2
>>> n = 2
>>> x = 5
>>> y = x ** n
>>> y
25

# using module pow(x, n)
>>> pow(x, n)
25
''')

# python2+3 - complex
# use 'j' suffix to set complex numbers ('i' is 'j' in python) j = sqrt(-1+0j)
# complex numbers have a 'real' and an 'imaginary' part
# python uses floats for 'real' and 'imaginary numbers'
print("set z = 3 + 5.7j")
z = 3 + 5.7j

# get type
print("get type:", type(z))

# print complex number representation
print("print(z):", z)

# print 'real' part value
print("print(z.real):", z.real)

# print 'imaginary' part value? - confusing output
print("print(z.imag):", z.imag)

# python2+3 - float
# floating point numbers
print("set e = 2.718281828")
e = 2.718281828
# get type
print("get type:", type(e))

# print float
print("print(e):", e)
print()

# floats can start with zeros but are stripped when printed
f = 000042.0002
print("print(f):", f)
print()

# python2
# wide to narrow numbers
# complex d > float c > long b > int a
#a = 2
#b = 3L
#c = 6.0
#d = 12 + 0j
# Rule: widen numbers so they are the same type

# python3
# wide to narrow numbers
# complex d > float c > int a
a = 2
c = 6.0
d = 12 + 0j
# Rule: widen numbers so they are the same type

# arithmetic
# python2 - addition int + long number
# widen int first, convert int to long > then add > result is long number
#a + b # int + long
#print(a + b) #
#5L

print("# python3 - addition int + float")
print(">>> int 2 > float 2.0 > add float 2.0 + float 6.0 = float 8.0")
print("a:", a, type(a), "\nc:", c, type(c), "\nprint(a + c)\n_result:", a + c, type(a + c))
print()

print("# python3 - substraction complex - float")
print(">>> float 6.0 > complex 6+0j > substract complex 12+0j - complex 6+0j = complex 6+0j")
print("c:", c, type(c), "\nd:", d, type(d), "\nprint(d - c)\n_result:", d - c, type(d - c))
print()

print("# python3 - multiplication int * complex")
print(">>> int 2 > complex 2+0j > multiply complex 2+0j * complex 12+0j = complex 24+0j")
print("a:", a, type(a), "\nd:", d, type(d), "\nprint(a * d)\n_result:", a * d, type(a * d))
print()

print("# python3 - division complex / float")
print(">>> float 6.0 > complex 6+0j > divide complex 12+0j / complex 6+0j = complex 2+0j")
print("d:", d, type(d), "\nc:", c, type(c), "\nprint(d / c)\n_result:", d / c, type(d / c))
print()

print("# python2 - division int whole numbers\n'16/5' returns quotient w/o remainder: 3\n'16 % 5' returns remainder\n'16/float(5)' returns float")
print()
print("# python3 - division int whole numbers\n'16/5' returns correct float")
a = 5
b = 16
print("a:", a, type(a), "\nb:", b, type(b), "\nprint(b / a)\n_result:", b / a, type(b / a))
print()

