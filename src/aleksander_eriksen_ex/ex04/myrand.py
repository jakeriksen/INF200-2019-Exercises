# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'




class LCGRand:
	a = 7 ** 5
	m = 2 ** 31 - 1

	def __init__(self, seed):
		self.seed = seed

	def rand(self):
		random = LCGRand.a * self.seed % LCGRand.m
		self.seed = random
		return random


class ListRand:
	def __init__(self, list_of_numbers):
		self.list_of_numbers = list_of_numbers
		self.idx = 0

	def rand(self):
		if self.idx >= len(self.list_of_numbers):
			raise RuntimeError('list index out of range, '
							   'rand() called too many times')
		number = self.list_of_numbers[self.idx]
		self.idx += 1
		return number
