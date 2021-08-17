import random

def play():
    user = input('(r)ock, (p)aper or (s)cissors? : ')
    # random choice from list elements
    computer = random.choice(['r','p','s'])

    if (user == 'S'):
        return f'SHOTGUN! Well, obviously you won ...'

    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return f'computer: {computer} - user: {user} You won!'

    if user == computer:
        return f'computer: {computer} - user: {user} Tie!'

    return f'computer: {computer} - user: {user} You lost!'

print(play())
