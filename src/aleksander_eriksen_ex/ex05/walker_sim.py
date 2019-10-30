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





class Simulation(Walker):
	def __init__(self, start, home, seed):
		"""
		Initialise the simulation

		Arguments
		---------
		start : int
			The walker's initial position
		home : int
			The walk ends when the walker reaches home
		seed : int
			Random generator seed
		"""
		self.start = start
		self.home = home
		self.seed = random.seed(seed)

	def single_walk(self):
		"""
		Simulate single walk from start to home, returning number of steps.

		Returns
		-------
		int
			The number of steps taken
		"""
		walk_ = Walker(self.start, self.home)
		while not walk_.is_at_home():
			walk_.move()
		return walk_.get_steps()


	def run_simulation(self, num_walks):
		"""
		Run a set of walks, returns list of number of steps taken.

		Arguments
		---------
		num_walks : int
			The number of walks to simulate

		Returns
		-------
		list[int]
			List with the number of steps per walk
		"""
		return [self.single_walk() for _ in range(num_walks)]





if __name__ == "__main__":
	num_walks = 20
	seed_twice = 12345
	seed_once = 54321
	sim_1 = Simulation(0, 10, seed_twice)
	sim_2 = Simulation(10, 0, seed_twice)
	sim_3 = Simulation(0, 10, seed_once)
	sim_4 = Simulation(10, 0, seed_once)

	from_0_to_10 = [walk for walk in sim_1.run_simulation(num_walks)]
	
	print(from_0_to_10)

"""
-  20 walks from start 0 to home 10
-  20 walks from start 10 to home 0
-  for each of those cases simulate *twice* with seed value 12345 and
   *once* with seed value 54321
-  print the resulting lists (six lists in total)."""