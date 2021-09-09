import sys

def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
            yield number
        else:
            number = number * 3 + 1
            print(number)
            yield number

try:
    while True:
        try:
            user = int(input('number: '))
            print(list(collatz(user)))
        # int() input validation
        except ValueError:
            print('enter an integer!')
except KeyboardInterrupt:
    print('',end='\n')
    sys.exit()
