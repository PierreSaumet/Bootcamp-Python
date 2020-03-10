#!/usr/bin/env python3

import sys

class GotCharacter:
	def __init__(self, first_name, is_alive=True):
		self.first_name = first_name
		self.is_alive = is_alive


class Lannister(GotCharacter):
	""" A class representing the Lannister family. Without them, GoT will be so fuck*** lame...
		Cersei die with her beloved brother Jaimie and Tyrion is doing weel"""
	def __init__(self, first_name=None, is_alive=True):
		""" super() method is too much complicated to understand, there is better option..."""
		super().__init__(first_name=first_name, is_alive=is_alive)
		#GotCharacter.__init__(self, first_name=first_name, is_alive=is_alive)
		self.family_name = "Lannister"
		self.house_words = "A Lannister always pays his debts."

	def print_house_words(self):
		print(self.house_words)

	def die(self):
		if self.is_alive:
			self.is_alive = False