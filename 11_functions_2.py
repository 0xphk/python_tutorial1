# socratia https://www.youtube.com/watch?v=NE97ylAnrz4&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=12
# print(dir())
import math

def f():
    pass

print('type of:\n def f():\n\tpass\n', type(f))

print('print(f) returns:', f, 'type:', f())

def ping():
    print('def ping() will return string "ping!"')
    return "ping!"
# print(ping())
a = ping()
print(a)

# print(dir())

# calculate volume of sphere [V = 4/3 π r³]
def volume(r):
    """returns the volume of a sphere with radius r [V = 4/3 π r³]
this uses math.pi() so we have to import it first: import math"""
    v = (4.0 / 3.0) * math.pi * r**3
    print('radius =', r)
    return v, r

# docstring is available using help(function)
#print(help(volume))

print(volume.__doc__, '\nvolume:', volume(4))

# calculate area of triangle [A = 1/2 b * h]
def area(b, h):
    """returns the area of a triangle [A = 1/2 b * h]"""
    print('side b', b, 'side h', h)
    return 0.5 * b * h
    # A = (1.0 / 2.0) * b * h
    # B = (0.5 * b) * h
    # return A, B

print(area(6, 32))

# keyword arguments are also called default arguments
# required arguments come first!
print('''\nrequired arguments before keyword arguments!
>>> argument order is important
>>> def g(x=0, y):
>>>     return x + y
>>> gives error
>>> required argument 'y' is defined after keyword argument 'x'
>>>
>>> def g(y, x=0):
>>>     return x + y
>>> works''')
def g(y, x=0):
    # arithmetic
    # return x + y
    # concatenated strings, then arithmetic, then single values
    return str(x) + str(y), x + y, x, y
print(g(1, 2))
# new class 'tuple' discovered
print(type(g(1, 2)))

print('''calculate inches and foot
>>> inch = 2.54 cm
>>> foor = 12 inches''')

# give *kwargs default values of 0
def cm(feet=0, inches=0):
    """converts a length from feet and inches to centimeters"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

print(cm(feet=5))
print(cm(inches=32))
print(cm(feet=5, inches=8))
print(cm(inches=8, feet=5),'cm')

