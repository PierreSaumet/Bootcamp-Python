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


def ft_pars(txt, n):
    all_items = []
    all_items = txt.split()
    count = 0
    count2 = 0
    new_list = []
    while count < len(all_items):
        if (len(all_items[count])) > int(n):
            new_list.append(all_items[count])
            count2 += 1
        count += 1
    return (new_list)


def ft_check(txt, n):
    tmp = str()
    i = 0
    count = 0
    for word in txt:
        for letter in word:
            if letter not in string.ascii_letters:
                while (word[i] != letter):
                    tmp += word[i]
                    i += 1
                txt[count] = tmp
                tmp = str()
                i = 0
        count += 1
    for word in txt:
        if word.isdigit():
            txt.remove(word)
    print(txt)

if __name__ == "__main__":
    len_arg = len(sys.argv)
    if len_arg != 3:
        print("ERROR")
    else:
        txt = sys.argv[1]
        n = sys.argv[2]
        if not n.isdigit() or txt.isdigit():
            print("ERROR")
        else:
            answer = ft_pars(txt, n)
            ft_check(answer, n)
