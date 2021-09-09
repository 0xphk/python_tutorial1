# exception handling inside and outside of functions
def spam(divideBy):
    return 42 // divideBy

# exception handing outside function
try:
    print(spam(2))
    print(spam(1.5))
    print(spam(0))  # stops execution of follow-up try expressions after raising error
    print(spam(3))
except ZeroDivisionError:
    # prints value + None as return None is added to every function without return statement
    print('spacetime error, division by zero')

# excepetion handling inside function
def spam2(divideBy):
    try:
        return 42 // divideBy
    except ZeroDivisionError:
        print('spacetime error, division by zero')

print(spam2(2))
print(spam2(1.5))
print(spam2(0))  # continues execution after raising division error inside function
print(spam2(3))
