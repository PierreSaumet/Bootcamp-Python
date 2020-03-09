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


MORSE_DICT = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----'}


def ft_getarg(len_arg):
    """This function returns a list which contains all arguments"""
    count = 1
    list_arg = []
    while count < len_arg:
        list_arg.append(sys.argv[count])
        count += 1
    return list_arg


def ft_alnum(word):
    """This function checks if "word" contains only alphanumeric characters"""
    """spaces and numeric characters, it returns 1 if there is an error"""
    error = 0
    for letter in word:
        if letter.isalnum() or letter.isspace() or letter.isalpha():
            pass
        else:
            error = 1
    return error


def ft_trad(word):
    """This function translate "word" into Morse code and return it"""
    text = str()
    for letter in word:
        if letter == ' ':
            text += '/ '
        else:
            text += MORSE_DICT[letter.upper()]
            text += ' '
    return (text)

if __name__ == "__main__":
    len_arg = len(sys.argv)
    error = 0
    trad = str()
    if len_arg > 1:
        list_words = ft_getarg(len_arg)
        for word in list_words:
            error = ft_alnum(word)
            if error == 1:
                print("ERROR")
                sys.exit()
            else:
                trad += ft_trad(word)
            trad += '/ '
        print(trad[:-2:])
