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


if __name__ == "__main__":
    len_arg = len(sys.argv)
    if (len_arg > 2):
        print("ERROR")
    elif (len_arg == 1):
        sys.exit(0)
    else:
        num = sys.argv[1]
        if (num.isnumeric()):
            if (int(num) == 0):
                print("I'm Zero.")
            elif (int(num) % 2) == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        else:
            print("ERROR")
