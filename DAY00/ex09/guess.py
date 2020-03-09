#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

#####################################
# Programme Python 3 Type           #
# Autor: Pierre Saumet, Paris, 2020 #
# Licence: GPL                      #
#####################################

#####################################
# Informations:
"""
    This is a program created with Python3.
    It respects the rules of PEP 8.
    Everything is in English.
    Python rocks.
"""
import sys
import string
import random

MENU = "This is an interactive guessing game!\nYou have t enter a number" \
       "between 1 and 99 to find out the secret number.\nType 'exit' to " \
       "end the game.Good luck!\n\n"

if __name__ == "__main__":
    print(MENU)
    answer = str()
    nbr = random.randint(1, 99)
    count = 0
    while answer != 'exit':
        answer = input("What's your guess between 1 and 99?\n")
        if not answer.isdigit():
            if answer == 'exit':
                pass
            else:
                print("That's not a number.")
        else:
            if int(answer) > nbr:
                if int(answer) > 99:
                    print("wesh tu ne sais pas lire? entre 1 et 99")
                print("Too high!")
            if int(answer) < nbr:
                print("Too low!")
            if int(answer) == nbr:
                if nbr == 42:
                    print("The answer to the ultimate question of lfe, the"
                          "universe and everything is 42.")
                count += 1
                if count == 1:
                    print("Congratuations! You got it on your first try!")
                else:
                    print("Congratuations you've got it!")
                print("You won in {} attempts!".format(count))
                sys.exit()
        count += 1
    print("Goodbye!")
