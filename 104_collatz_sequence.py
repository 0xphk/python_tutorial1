""" personal notes:

    # should run it but it doesn't
    collatz(user)

    # this actually runs the function but i have not f*cking idea why
    list(collatz(user))

    # runs function and prints list 
    print(list(collatz(user)))
"""
import sys
from modules import treset

treset()

print('computes collatz seq [ (even) n // 2 || (odd) n * 3 + 1 ] for given number\n')

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number //= 2  # number = number // 2 in short
            print(number, end=' ')
            yield number  # requires yield instead of return
            """ personal notes:
                - yield statement makes a generator out of this function
                - some sort of updating value and return it back to function ?
                - return statement seems to exit function call instead of returning value back to function
            """
        else:
            number = number * 3 + 1  # can not be shortened like (number *= 3 + 1) :(
            print(number, end=' ')
            yield number

try:
    while True:
        try:
            user = int(input('enter number: '))
            if user < 0:
                print('no negative feelings please ...')
                continue
            print('collatz seq: ', end='')
            list(collatz(user))  # this calls collatz() no f*cking idea why collatz(user) doesn't
            print()
            break

        except ValueError:  # int() input validation
            print('not a number')

except KeyboardInterrupt:
    print()
    sys.exit()
