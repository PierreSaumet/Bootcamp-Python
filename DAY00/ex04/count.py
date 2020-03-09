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


def display_txt(string):
    str1 = "Sum:\t\t{}\nDifference:\t{}\nProduct:\t{}" \
            "\nQuotient:\t{}\nRemainder:\t{}"
    print(str1.format("1", "2", "3", "4", "5"))


def ft_full(num1, num2):
    summary = int(num1) + int(num2)
    diff = int(num1) - int(num2)
    product = int(num1) * int(num2)
    quot = int(num1) / int(num2)
    remainder = int(num1) % int(num2)
    return (str(summary), str(diff), str(product), str(quot), str(remainder))

if __name__ == "__main__":
    len_arg = len(sys.argv)
    str1 = "Sum:\t\t{}\nDifference:\t{}\nProduct:\t{}" \
        "\nQuotient:\t{}\nRemainder:\t{}"
    if (len_arg > 3):
        print("InputError: too many arguments\n")
        print("Usage: python operations.py")
        print("Example:")
        print("\tpython operations.py 10 3")
    elif (len_arg <= 2):
        print("Usage: python operations.py")
        print("Example:")
        print("\tpython operations.py 10 3")
    else:
        num = sys.argv[1]
        num2 = sys.argv[2]
        if (type(num) == str or type(num2) == str) and (
                num.isnumeric() is False or num2.isnumeric() is False):
            print("InputError: only numbers\n")
            print("Usage: python operations.py")
            print("Example:")
            print("\tpython operations.py 10 3")
        elif (int(num2) == 0):
            print(str1.format(
                                num, num, 0, "ERROR (div by zero)",
                                "ERROR (modulo by zero)"))
        else:
            summary, diff, products, quo, rem = ft_full(num, num2)
            print(str1.format(summary, diff, products, quo, rem))
