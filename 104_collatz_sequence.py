import sys
from modules import treset

treset()

print('computes collatz seq for given number\n')

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            # number = number // 2 or in short
            number //= 2
            print(number, end=' ')
            yield number
            # requires yield - makes a generator out of this function
            # some sort of updating value and return it to function?
            # instead of return which seems to exit function call
        else:
            number = number * 3 + 1
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
            # this actually runs the collatz() function and i have not f*cking idea why
            list(collatz(user))
            print()
            break
        except ValueError:  # int() input validation
            print('not a number')
except KeyboardInterrupt:
    print()
    sys.exit()

# should run it but it doesn't
#collatz(user)

# this actually runs the function but i have not f*cking idea why
#list(collatz(user))

# runs function and prints list as well
#print(list(collatz(user)))

#print(end='\n\n')
