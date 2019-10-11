# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Eirik Høyheim'
__email__ = 'jaer@nmbu.no', 'eirihoyh@nmbu.no'

from random import randint


def throw_dice():
	return randint(1, 6)


def single_game(num_players):
	snake_ladder = {1 : 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
					24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

	player_pos = [0] * num_players # Initializing player positions
	player_moves = [0] * num_players # Initializing player moves

	for game in range(num_players): # Going through each players game

		while player_pos[game] < 90: # Done when player reaches 90
			player_pos[game] += throw_dice() # adding dice-value to position

			# Checking if player position is in snake or ladder position
			# If so, it replaces the position accordingly.
			if player_pos[game] in snake_ladder:
				player_pos[game] = snake_ladder[player_pos[game]]

			player_moves[game] += 1 # moves/turns of the player

	sort_moves = sorted(player_moves) # sorting player moves (low to high)
	winner = sort_moves[0] # player with lowest moves wins

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
		List with the numbedr of moves needed in each game.
	"""


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
		List with the numbedr of moves needed in each game.
	"""
