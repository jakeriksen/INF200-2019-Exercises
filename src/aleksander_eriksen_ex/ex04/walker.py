# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

import random


class Walker:
	def __init__(self, start, home):
		self.pos_x = start
		self.home = home
		self.steps = 0

	def move(self):
		random_step = random.randint(0, 1)  # Need to use randint()
		if random_step == 0:
			random_step = -1
		self.pos_x += random_step  # Would rather use random.choice([-1, 1])
		self.steps += 1

	def is_at_home(self):
		if self.pos_x == self.home:
			return True
		return False

	def get_position(self):
		return self.pos_x

	def get_steps(self):
		return self.steps


def walk(start, home):
	drunk_walker = Walker(start, home)
	while not drunk_walker.is_at_home():
		drunk_walker.move()
	return drunk_walker.get_steps()


if __name__ == "__main__":
	distances = [1, 2, 5, 10, 20, 50, 100]
	simulations = 5

	for distance in distances:
		list_walk = [walk(0, distance) for _ in range(simulations)]
		print(f'Distance: {distance:4d} -> Path lengths: {list_walk}')
