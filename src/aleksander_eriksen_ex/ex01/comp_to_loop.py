def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]



def squares_by_loop(n):
    list = []
    for number in range(n):
        if number % 3 is 1:
            list.append(number**2)
    return list


if __name__ == '__main__':
    number = 9
    if squares_by_comp(number) != squares_by_loop(number):
        print('ERROR!')


