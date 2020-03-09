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


my_tuple = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    print("day_%.2d, ex_%.2d : %.2f, %.2e, %.2e" % my_tuple)
