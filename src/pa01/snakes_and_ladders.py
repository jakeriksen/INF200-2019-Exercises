# -*- coding: utf-8 -*-

__author__ = 'Aleksander Eriksen', 'Eirik Høyheim'
__email__ = 'jaer@nmbu.no', 'eirihoyh@nmbu.no'

from random import randint


def throw_dice():
    return randint(1, 6)


def single_game(num_players):
    snake_ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85,
                    24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}

    player_pos = [0] * num_players
    player_moves = [0] * num_players
    for game in range(num_players):

        while player_pos[game] < 90:
            player_pos[game] += throw_dice()

            if player_pos[game] in snake_ladder:
                player_pos[game] = snake_ladder[player_pos[game]]

            player_moves[game] += 1

    sort_moves = sorted(player_moves)
    winner = sort_moves[0]

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
