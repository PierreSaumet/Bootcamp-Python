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
    Everythings is in English.
    Python rocks.
"""
import sys
import string


def ultime_fct(txt):
    """This function returns 4 variables which contain the data needed"""
    low = 0
    upp = 0
    space = 0
    punc = 0
    for letter in txt:
        if letter.islower():
            low += 1
        elif letter.isupper():
            upp += 1
        elif letter in string.punctuation:
            punc += 1
        elif letter.isspace():
            space += 1
    return (low, upp, space, punc)


def ft_text(sum_str, upp, low, punc, space):
    """This function display the result"""
    print("The text contains ", sum_str, "characters:")
    print("- ", upp, " upper letters")
    print("- ", low, " lower letters")
    print("- ", punc, " punctuation marks")
    print("- ", space, " spaces")


def text_analyzer(*args):
    """This function counts the number of upper characters, lower characters"""
    """punctuation and spaces in a given text. It uses 2 other functions"""
    low = 0
    upp = 0
    space = 0
    punc = 0
    if len(args) == 0:
        var = input()
        low, upp, space, punc = ultime_fct(var)
        sum_string = len(var)
        ft_text(sum_string, upp, low, punc, space)
    else:
        if len(args) >= 2:
            print("ERROR")
        else:
            sum_string = len(args)
            low, upp, space, punc = ultime_fct(args)
            ft_text(sum_string, upp, low, punc, space)
