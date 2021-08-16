# freecodecamp [https://www.youtube.com/watch?v=8ext9G7xspg]
import random

def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f'guess a number between 1 and {x}: '))
        if guess < randomNumber:
            print('guess too low')
        elif guess > randomNumber:
            print('guess too high')
    print(f'you guessed {randomNumber} right!')

guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'is {guess} too (L)ow, too (H)igh, or maybe (C)orrect? : ')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print('yay')

print('number to guess: ',random.randint(1,1000))
computer_guess(1000)
