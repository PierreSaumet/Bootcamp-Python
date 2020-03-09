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
import argparse


def reverse_string(string):
    return string[::-1]


def swap_case(string):
    return (string.swapcase())

if __name__ == "__main__":
    str_ultime = ""
    for arg in sys.argv[1::]:
        str_ultime += arg
        str_ultime += " "
    str_ultime = reverse_string(str_ultime)
    str_ultime = swap_case(str_ultime)
    print(str_ultime[1:])
