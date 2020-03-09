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


cookbook = {"sandwich": {"ingredients": ["ham", "bread", "cheese", "tomatoes"],
            "meal": "lunch", "prep_time": 10},
            "cake": {"ingredients": ["flour", "sugar", "eggs"],
                     "meal": "dessert", "prep_time": 60},
            "salad": {"ingredients": ["avocado", "arugula", "spinach"],
                      "meal": "dessert", "prep_time": 60}}


def print_recipe(name):
    """This function displays a recipe"""
    print("Recipe for", name, ":")
    print("Ingredients list: {}.".format(cookbook[name]["ingredients"]))
    print("To be eaten for {}.".format(cookbook[name]["meal"]))
    print("Takes {} minute(s) of"
          "cooking.\n\n".format(cookbook[name]["prep_time"]))


def delete_recipe(name):
    """This function deletes a recipe"""
    del cookbook[name]


def add_recipe(name, ingre, type_meal, time):
    """This function add a recipe"""
    sub_dict = {}
    sub_dict["ingredients"] = ingre
    sub_dict["meal"] = type_meal
    sub_dict["prep_time"] = time
    cookbook[name] = sub_dict


def print_all():
    """This function displays the cookbook"""
    for key in cookbook.keys():
        print_recipe(key)
        print("\n\n")


def print_main_menu():
    "This function displays the main menu"""
    print("\tPlease select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    answer = input()
    print("\n")
    return answer


if __name__ == "__main__":
    menu = 1
    while (menu):
        answer = print_main_menu()
        if (answer.isdigit()):
            if (int(answer) == 1):
                name = input("What is the name of the recipe?\t")
                while not name:
                    name = input("What is the name of the recipe?\t")
                ing = input("What are the ingredients?"
                            "put a space between them ...\t")
                while not ing:
                    ing = input("What are the ingredients?"
                                "put a space between them ...\t")
                ing2 = ing.split()
                time = input("How long to cook it?\t")
                while not time:
                    time = input("How long to cook it?\t")
                kind_of = input("What is it? a dessert? a meal?"
                                "a breakfast? ...\t")
                while not kind_of:
                    kind_of = input("What is it? a dessert? a meal?"
                                    "a breakfast? ...\t")
                add_recipe(name, ing2, kind_of, time)
            elif (int(answer) == 2):
                print("What recipe do you want to delete?\n")
                for key in cookbook.keys():
                    print(key)
                to_del = input()
                while to_del not in cookbook.keys():
                    to_del = input("What recipe do you want to delete?\t")
                delete_recipe(to_del)
            elif (int(answer) == 3):
                print("What is the name of the recipe do you want to print?\t")
                for key in cookbook.keys():
                    print(key)
                to_print = input("\n")
                while to_print not in cookbook.keys():
                    print("No, it doesn't exit...")
                    print("What is the name of the recipe do you want"
                          "to print?\t")
                    for key in cookbook.keys():
                        print(key)
                    to_print = input("\n")
                print_recipe(to_print)
            elif (int(answer) == 4):
                print_all()
            elif (int(answer) == 5):
                print("Thank you bye bye\nCookbook closed.")
                menu = 0
            else:
                print("\nError try again\n\n")
        else:
            print(
                "This option does not exist, please type the corresponding"
                "number.\nPrint a corresponding number")
            print("to exit, enter 5.\n")
