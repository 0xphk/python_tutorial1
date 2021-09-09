# does not work yet
import sys

print()

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            #number = number // 2
            # same as above but shorter
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
    try:
        while True:
            user = int(input('enter number: '))

            if user < 0:
                print('no negative feelings please ...')
                break

            print('collatz seq: ', end='')
            list(collatz(user))
            print()
            break

    # int() input validation
    except ValueError:
        print('not a number')

except KeyboardInterrupt:
    print()
    sys.exit()

#try:
#    while True:
#        try:
#            user = int(input('enter integer: '))
#            
#            if user < 0:
#                print('only postive numbers')
#            continue
#
#            list(collatz(user))
#            print(list(collatz(user)))
#        # int() input validation
#        except ValueError:
#            print('enter a number')
#except KeyboardInterrupt:
#    print('',end='\n')
#    sys.exit()

# should run it but it doesn't
# collatz(user)

# works but i have no f*cking idea why
#print('collatz seq: ', end='')
#try:
#    list(collatz(user))
#except:
#    print('did not work, try using integer')

# runs function and prints list as well
#print(list(collatz(user)))

#print(end='\n\n')
