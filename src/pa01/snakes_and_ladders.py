# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Eirik Høyheim'
__email__ = 'jaer@nmbu.no', 'eirihoyh@nmbu.no'

import random
import numpy as np


def throw_dice():
	return random.randint(1, 6)


def single_game(num_players):
	snake_ladder = {1 : 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
					24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

	player_pos = [0] * num_players  # Initializing player positions
	player_moves = [0] * num_players  # Initializing player moves

	for game in range(num_players):  # Going through each players game

		while player_pos[game] < 90:  # Done when player reaches 90
			player_pos[game] += throw_dice()  # adding dice-value to position

			# Checking if player position is in snake or ladder position
			# If so, it replaces the position accordingly.
			if player_pos[game] in snake_ladder:
				player_pos[game] = snake_ladder[player_pos[game]]

			player_moves[game] += 1  # moves/turns of the player

	winner = min(player_moves)  # player with lowest moves wins

	return winner


def multiple_games(num_games, num_players):
	"""
	Returns durations of a number of games.

	Arguments
	---------
	num_games : int
		Number of games to play
	num_players : int
		Number of players in the game

	Returns
	-------
	num_moves : list
		List with the number of moves needed in each game.
	"""
	return [single_game(num_players) for _ in range(num_games)]


def multi_game_experiment(num_games, num_players, seed):
	"""
	Returns durations of a number of games when playing with given seed.

	Arguments
	---------
	num_games : int
		Number of games to play
	num_players : int
		Number of players in the game
	seed : int
		Seed used to initialise the random number generator

	Returns
	-------
	num_moves : list
		List with the number of moves needed in each game.
	"""
	random.seed(seed)
	return multiple_games(num_games, num_players)


if __name__ == "__main__":
	game_simulation = sorted(multi_game_experiment(100, 4, 3))

	shortest_game = min(game_simulation)
	longest_game = max(game_simulation)
	median_game = np.median(game_simulation)
	mean_game = np.mean(game_simulation)
	std_deviation = np.std(game_simulation)

	print(f'The shortest game was {shortest_game} moves, \n'
		  f'and the longest game was {longest_game} moves.')

	print(f'\nThe median game duration was {median_game} moves')

	print(f'The mean game duration was {mean_game:.1f} moves, \n'
		  f'and its standard deviation is {std_deviation:.1f}.')
