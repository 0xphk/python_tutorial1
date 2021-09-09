import sys

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number, end='')
            # requires yield (some sort of updating value and return it to function?)
            # instead of return which seems to exit function call
            yield number
            #return number
        else:
            number = number * 3 + 1
            print(number, end='')
            yield number
            #return number

try:
    try:
        user = int(input('number: '))

    # int() input validation
    except ValueError:
        print('enter an integer!')

except KeyboardInterrupt:
    print('',end='\n')
    sys.exit()

# should run it but it doesn't
# collatz(user)

# works but i have no f*cking idea why
list(collatz(user))

# calling it this way seems to be the only way to get this work
# this expression runs it to create list
#print(list(collatz(user)))
