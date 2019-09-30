# from ..ex01.letter_counts import letter_freq
import numpy as np


# Didn't manage to import letter_freq from its own directory
def letter_freq(txt):
    txt = sorted(txt.lower())  # sorted() sorts the characters in alphabetical order, while txt.lower lowers the text
    freq = {}  # Making a dictionary for the frequency

    for character in txt:  # Running through the characters, then adding the characters into the dict and counts them
        if character not in freq.keys():  # Checking if the key is there, 'else' it adds +1 to the counter
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
