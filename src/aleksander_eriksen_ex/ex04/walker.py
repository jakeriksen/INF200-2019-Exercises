# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

import random


class Walker:
	def __init__(self, start, home):

		"""
		param start: initial position of the walker
		param home: final/goal position of the walker
		"""
		self.pos_x = start
		self.home = home
		self.steps = 0

	def move(self):
		"""Changes the position by -1 or +1 along the 1D route
		"""
		random_step = random.randint(0, 1)  # Need to use randint()
		if random_step == 0:
			random_step = -1
		self.pos_x += random_step  # Would rather use random.choice([-1, 1])
		self.steps += 1

	def is_at_home(self):
		"""Returns True if walker is at home position.
		"""
		if self.pos_x == self.home:
			return True
		return False

	def get_position(self):
		"""Returns current position.
		"""
		return self.pos_x

	def get_steps(self):
		"""Returns steps taken
		"""
		return self.steps


def walk(start, home):
	"""Returns how many steps taken until walker is home
	"""
	drunk_walker = Walker(start, home)
	while not drunk_walker.is_at_home():
		drunk_walker.move()
	return drunk_walker.get_steps()


if __name__ == "__main__":
	distances = [1, 2, 5, 10, 20, 50, 100]
	simulations = 5
	random.seed(2)  # Fastest seed I found
	for distance in distances:
		list_walk = [walk(0, distance) for _ in range(simulations)]
		print(f'Distance: {distance:4d} -> Path lengths: {list_walk}')
