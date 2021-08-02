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
    A = (1.0 / 2.0) * b * h
    B = (0.5 * b) * h
    return A, B

print(area(2, 13))
