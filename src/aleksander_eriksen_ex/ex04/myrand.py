# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

a = 7 ** 5
m = 2 ** 31 - 1


class LCGRand:
	def __init__(self, seed):
		self.seed = seed

	def rand(self):
		random = a * self.seed % m
		self.seed = random
		return random


class ListRand(LCGRand):
	def __init__(self, list_of_numbers):
		self.list_of_numbers = list_of_numbers





