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


if __name__ == "__main__":
    phrase = "The right format"
    count = 0
    string = ""
    if (len(phrase) == 42):
        print(phrase)
    elif (len(phrase) > 42):
        print(phrase[:42:])
    else:
        while (count < (42 - len(phrase))):
            string += "-"
            count += 1
        print(string + phrase, end='')
