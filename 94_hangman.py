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
    print(word)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        # letters used as string ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('Used letters : ', ' '.join(used_letters))

        # print current solve status ie (W - R D)
        # letter defined in 'for letter in word' loop at eol
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(word_list)
        print('current word : ', ' '.join(word_list))

        # get user input
        user_letter = input('guess a letter : ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('Already used character ... try again! ')

        else:
            print('Invalid character! ')

    print('final word : ', ' '.join(word))

hangman()
