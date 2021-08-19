# based on freecodecamp 12 python beginner projects
# [https://www.youtube.com/watch?v=8ext9G7xspg]
# [https://github.com/kying18/hangman]

from words import words
from modules import treset
import random
import string

treset()

def get_valid_word(words):
    word = random.choice(words)

    # only get words w/o dash or whitespace
    while '-' in word or ' ' in word:
        word = random.choice(word)

    # return upper() fixed in github
    return word.upper()

def hangman():
    word = get_valid_word(words)

    # debug
    # print(word)

    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = int()
    difficulty = str()

    # no need for dual input() if difficulty is set to str() before while loop
    # difficulty = input('Enter difficulty: (E)asy, (D)ynamic, (K) or (S)oulslike? : ')

    # while (difficulty.upper() != 'E') or (difficulty.upper() != 'D') or (difficulty.upper() != 'K') or (difficulty.upper() != 'S'):
    # ^_ way too long, looks like this can be combined in one statement which is really nice
    while difficulty.upper() != 'E' != 'D' != 'K' != 'S':

        difficulty = input('Enter difficulty: (E)asy, (D)ynamic, (K) or (S)oulslike? : ')

        if difficulty.upper() == 'E':
            print(f"{difficulty.upper()} - Easy equals 10 lives")
            lives = 10
            break

        elif difficulty.upper() == 'D':
            print(f"{difficulty.upper()} - Dynamic lives based on word length")
            lives = len(word_letters)
            break

        elif difficulty.upper() == 'S':
            print(f"{difficulty.upper()} - Soulslike equals 1 live, happy dying!")
            lives = 1
            break

        elif difficulty.upper() == 'K':
            print(f"You ({difficulty.upper()})illed yourself !")
            lives = 0
            break

        print('Invalid choice!')

    while len(word_letters) > 0 and lives > 0:
        # letters used as string ' '.join(['a', 'b', 'cd']) --> 'a b cd'

        # w/o visual
        # print('Used letters : ', ' '.join(used_letters))

        # w/ visual
        print('You have', lives, 'lives left and used these letters : ', ' '.join(used_letters))

        # current solve status ie (W - R D), letter defined in 'for letter in word' loop at eol
        word_list = [letter if letter in used_letters else '-' for letter in word]

        # visual
        print(lives_visual_dict[lives])
        print('Current word : ', ' '.join(word_list))

        # get user input
        user_letter = input('Guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives -= 1
                print('Your letter,', user_letter, 'is not in the word\nLives left:',lives)

        elif user_letter in used_letters:
            print('Already used character ... try again! ')

        else:
            print('Invalid character! ')

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died and lost all your souls ! the word was: ',word)

    else:
        print('Yay, you won, final word : ', ' '.join(word))

# visual representation
lives_visual_dict = {
    0: """
            _________
           | /      |
           |/      ( )
           |        |
           |       / \\
           |
       """,
    1: """
            _________
           | /      |
           |/      ( )
           |        |
           |       /
           |
        """,
    2: """
            _________
           | /      |
           |/      ( )
           |        |
           |
           |
        """,
    3: """
            _________
           | /      |
           |/      ( )
           |
           |
           |
        """,
    4: """
            _________
           | /      |
           |/
           |
           |
           |
        """,
    5: """
            _________
           | /
           |/
           |
           |
           |
        """,
    6: """
            _________
           |
           |
           |
           |
           |
        """,
    7: """
           |
           |
           |
           |
           |
        """,
    8: """
           |
           |
           |
           |
        """,
    9: """
           |
           |
           |
        """,
    10: "",
}

hangman()
