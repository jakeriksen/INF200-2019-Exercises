import random as rd

__author__ = 'Aleksander Eriksen'
__email__ = 'jaer@nmbu.no'

'''
--------- best_game_ever -----------
The original code of this guessing-game made you guess a number between 2 
and 12. This will too.
You got 3 tries, and the max score you can gain is probably 1 (if you're 
lucky). Actually 3 if you're very lucky. 
Yes, it is a terrible and frustrating game.

The original code was even more terrible. Now it's understandable.
------------------------------------
'''


def guess_number():
	return int(input('Guess a number between 2 and 12: '))


def random_number():  # Gives you a random number/integer between (and
    # including) 2 and 12.
	return rd.randint(2,
					  12)  # Original code consisted of " rd.randint(1,
    # 6) + rd.randint(1,6) ".


def run_hard_guessing_game():
	tries = 3
	random = random_number()
	while tries > 0:
		guess = guess_number()
		if guess is not random:  # If your guess is not correct (aka the
            # random number), you lose your tries.
			print('Wrong, try again!')
			tries -= 1

	if tries > 0:
		print(f'You won {tries} points')

	else:
		print(f'You lost. Correct answer: {random}')


if __name__ == '__main__':
	run_hard_guessing_game()
