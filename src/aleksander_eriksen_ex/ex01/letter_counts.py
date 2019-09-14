def letter_freq(txt):
    txt = sorted(txt.lower())  # sorted() sorts the characters in alphabetical order, while txt.lower lowers the text
    freq = {}  # Making a dictionary for the frequency

    for character in txt:  # Running through the characters, then adding the characters into the dict and counts them
        if character not in freq.keys():  # Checking if the key is there, 'else' it adds +1 to the counter
            freq[character] = 1
        else:
            freq[character] += 1

    return freq


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
