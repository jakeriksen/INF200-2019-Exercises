SUITS = ('C', 'S', 'H', 'D')  # Defining the suits.
VALUES = range(1, 14)  # Got the values from 1 to 13.


def deck_loop():
	deck = []
	for suit in SUITS:
		for val in VALUES:
			deck.append((suit, val))
	return deck


# The list comprehension of the code above:
def deck_comp():
	deck = [(suit, val) for suit in ('C', 'S', 'H', 'D') for val in
			range(1, 14)]
	return deck


if __name__ == '__main__':
	if deck_loop() != deck_comp():
		print('ERROR!')
