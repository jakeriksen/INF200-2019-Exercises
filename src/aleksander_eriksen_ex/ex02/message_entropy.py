# from ..ex01.letter_counts import letter_freq
import numpy as np


def letter_freq(txt):
	txt_ = sorted(txt.lower())  # Sort lower text
	freq = {}  # Making a dictionary for the frequency

	for character in txt_:  # Character checker and counter
		if character not in freq.keys():
			freq[character] = 1
		else:
			freq[character] += 1

	return freq


def entropy(message):
	"""
	Uses the function letter_freq() to count the occurrences of the symbols.
	Then uses the formula for entropy and calculates it.


	Parameters
	----------
	message

	Returns
	-------
	entropy
	"""

	frequency = letter_freq(message)
	n = len(message)
	entropy_ = []
	for n_i in frequency.values():
		p_i = n_i / n
		h = - p_i * np.log2(p_i)
		entropy_.append(h)
	return sum(entropy_)


if __name__ == "__main__":
	for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
		print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
