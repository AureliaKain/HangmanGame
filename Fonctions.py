from random import randrange
from Donnees import *

def word_selection(words_list):
    nb_words = len(words_list)
    word_selected = words_list[randrange(0, nb_words-1)]
    return word_selected

def display_word():
    """display the word with discovered letters. Non discovered letters are replaced by *"""


def fill_word():
    """add discovered letters to the word"""

def letter_check(letter_to_check, word, word_to_fill):
    """check whether the letter selected is in the word. If yes, return its position"""
    letter_index = []
    word_to_list = list(word)
    for index, letter in enumerate(word):
        if letter_to_check == letter:
            letter_index.append(index)
            good_letter = letter
        else:
            continue
    if len(letter_index) > 0:
        print('well done, you guessed a letter!')
        for i in letter_index:
            word_to_fill[i] = good_letter
        print(word_to_fill)
        if word_to_list == word_to_fill:
            print('Congrats, you guessed the word!')
            return 2
        else:
            print('You still have letters to guess')
            return 1
    else:
        print('Sorry, your letter is not in the word to guess!')
        return 0

# def score_partie():
#     xxx
# 
# def score_total(name, dd):
#     xxxxx if new, 0 else incrementer
