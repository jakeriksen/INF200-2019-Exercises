def letter_freq(txt):
    text = sorted(txt.lower())
    freq = {}

    for character in text:
        if character not in freq.keys():
            freq[character] = 1
        else:
            freq[character] += 1



    return freq

if __name__ == '__main__':
    text = input('Please enter text to analyse: ')




    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))


