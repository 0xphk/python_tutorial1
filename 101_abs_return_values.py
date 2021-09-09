# special data Type None in python is used for return values in every function which does not contain any return statement
# alyways used as retun value in print() function

print('return value of print():', type(print()))

def ret():
    print('return')
    # single return statement always evaluates to None
    # return
    # some as above, always added by python if no return statement set
    return None

ret()
print(type(ret()))

# call stack
def a():
    print('a starts')
    b()
    d()
    print('a returns')

def b():
    print('b starts')
    c()
    print('b returns')

def c():
    print('c starts')
    print('c returns')

def d():
    print('d starts')
    print('d returns')

a()
