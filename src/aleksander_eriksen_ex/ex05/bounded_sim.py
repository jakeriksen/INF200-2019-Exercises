# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

from walker_sim import Walker
import random


class BoundedWalker(Walker):
	def __init__(self, start, home, left_limit, right_limit):
		"""
		Initialise the walker

		Arguments
		---------
		start : int
			The walker's initial position
		home : int
			The walk ends when the walker reaches home
		left_limit : int
			The left boundary of walker movement
		right_limit : int
			The right boundary  of walker movement
		"""
		super().__init__(start, home)
		self.start = start
		self.home = home
		self.left_limit = left_limit
		self.right_limit = right_limit

	def move(self):
		"""Defining the limits (left, right) for the one dimensional axis
		"""
		super().move()

		if self.pos_x > self.right_limit:
			self.pos_x = self.right_limit

		if self.pos_x < self.left_limit:
			self.pos_x = self.left_limit


class BoundedSimulation(BoundedWalker):
	def __init__(self, start, home, seed, left_limit, right_limit):
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
		left_limit : int
			The left boundary of walker movement
		right_limit : int
			The right boundary  of walker movement
		"""
		super().__init__(start, home, left_limit, right_limit)
		self.seed = random.seed(seed)

	def single_walk(self):
		"""
		Simulates a single walk from start to finish, where move() is limited

		Returns
		-------
		int
			The number of steps taken

		"""
		walk_ = BoundedWalker(self.start, self.home, self.left_limit,
							  self.right_limit)

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
	seed_ = 1
	boundaries = [0, -10, -100, -1000, -10000]

	print('\nSimulations - from 0 to 20 - seed (1) - Right boundary (20)\n')
	for boundary in boundaries:
		sim = BoundedSimulation(0, 20, seed_, boundary, 20).run_simulation(20)
		print(f'Left boundary -->  {boundary:6d}:  {sim}')
