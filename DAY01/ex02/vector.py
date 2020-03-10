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
from math import *
class Vector:
    def __init__(self, data):
        self.data = data
        self.x = 0.0
        self.tmp = list()
        self.len_data = int()
        if isinstance(self.data, int) == True:
            if self.data < 0:
                self.data = -self.data
            if self.data == 0:
                self.tmp.append(self.x)
            while self.data > 0:
                self.tmp.append(self.x)
                self.x += 1
                self.data -= 1
            print(self.tmp)
            self.data = self.tmp
            self.len_data = len(self.data)
        if isinstance(self.data, list) == True:
            for item in self.data:
                if isinstance(item, float) == False:
                    raise Exception("Sorry, only floats")
            self.len_data = len(self.data)
        if isinstance(self.data, tuple) == True:
            for item in self.data:
                if isinstance(item, (int, float)) == False:
                    raise Exception("Sorry, only floats or integers")
            if len(self.data) != 2:
                raise Exception("Sorry, only 2 numbers")
            if self.data[0] < self.data[1]:
                x = self.data[0]
                while x < self.data[1]:
                    self.tmp.append(x * 100.0 / 100.0)
                    x += 1
                self.data = self.tmp
            self.len_data = len(self.data)
        
    def __add__(self, other):
        """
            Override l'opérateur +
        """
        tmp = list()
        count = 0
        if isinstance(other, int) == True:
            tmp = list()
            for item in self.data:
                tmp.append(item + other)
        #print(tmp, "et data=", self.data)
        elif isinstance(other, Vector) == True:
            print("here", len(other.data), other.data)
            if len(other.data) == self.len_data:
                while count < self.len_data:
                    tmp.append(self.data[count] + other.data[count])
                    count += 1
            return Vector(tmp)


            """if len(other) != self.len_data:
                raise Exception("Sorry, only vector of same direction")
            else:
                while count < len(other):
                    tmp.append(self.data[count])
                    count += 1"""
        else:
            print("la", type(other))
        return tmp

                  
    def __str__(self):
        """Return a string to print with informations"""
        txt_to_display = "This vector has {} dimension(s).\nIt contains: {}\n"
        return self.__class__.__name__ + str(self.data)

    def __repr__(self):
        """Return a python expression with informations"""
        txt_to_display = "This vector has {} dimension(s).\nIt contains: {}\n"
        return self.__class__.__name__ + str(self.data)