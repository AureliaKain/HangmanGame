# -*-coding:utf-8 -*
from Donnees import *
from Fonctions import *

#Ce fichier contient le code d'un jeu de pendu

try:
    name = input('Hi! What\'s your name?')
except ValueError:
    print("vous n'avez pas saisi un nom")

print ('Hi {name}, let\'s play!'.format(name=name))

keep_going = True
while keep_going == True:

    print('You have 8 lifes to guess the word')
    #Generate the word to guess
    word_selected = word_selection(words_list)
    word_empty= []
    for i in enumerate(word_selected):
        word_empty.append('*')
    print(word_empty)

    #Start to guess
    # Step 1 - Letter selection
    print('Now it\'s time to guess the word!')
    i=0
    #print(word_selected)
    while i <= attempts_nb:
        life = i
        print('you used {}/8 lifes'.format(life))
        try:
            letter = input('Please select a letter:')
            assert len(letter) == 1 and type(letter) == str
        except AssertionError:
            if len(letter) == 0:
                print('you don\'t enter a letter')
            if len(letter) > 1:
                print('you enter more than one letter')
            if type(letter) != str:
                print('you don\'t enter a letter')
    # step 2 - check if the letter is in the word
        #letter_check(letter, word_selected, word_empty)
        if letter_check(letter,  word_selected, word_empty) == 2:
            score_partie = attempts_nb - i
            break
        elif letter_check(letter,  word_selected, word_empty) == 1:
            continue
        elif letter_check(letter, word_selected, word_empty) == 0:
            i+=1

    if i == 9:
        print('Sorry, you loose the game! The word was {}'.format(word_selected))
        print('You gain 0 point')


    keep_going = input('Do you want to continue the game?(True or False)')
    if keep_going != True or False:
        print("You've to answer by True or False")
        keep_going = input('Do you want to continue the game?(True or False)')

#
# display the word empty
#
# numbers of attempts = xxxxx