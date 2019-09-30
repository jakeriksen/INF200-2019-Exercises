def squares_by_comp(n):
    return [k ** 2 for k in range(n) if k % 3 == 1]


# Rewritten the code from list comprehension to a loop
def squares_by_loop(n):
    squares = []
    for k in range(n):  # Iterates over the range of number you choose
        if k % 3 == 1:  # Gives a sequence with 3 numbers between. 1, 4, 7, 13... (depending on the range)
            squares.append(k ** 2)  # Squares the given number and adds it to the list
    return squares


if __name__ == '__main__':
    number = 9
    if squares_by_comp(number) != squares_by_loop(number):
        print('ERROR!')
