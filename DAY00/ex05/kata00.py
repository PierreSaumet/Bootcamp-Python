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

t = (19, 42, 21)

if __name__ == "__main__":
    len_t = len(t)
    string = ""
    for i in t:
        string += str(i)
        string += ", "
    len_string = len(string)
    next_string = string[0:len_string-2]
    print("The {} numbers are: {}".format(len_t, next_string))
