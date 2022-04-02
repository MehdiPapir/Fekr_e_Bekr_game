def number_population(num, array):
    return len(list(filter(lambda x: x == num, array)))


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 1, 2, 5, 4, 5, 2, 1, 4, 5, 2, 3, 2, 5, 1, 2, 3, 5, 2, 1, 4, 5,
                 2, 3, 5, 2, 1, 4, 5, 3, 2, 5, 1, 4, 2, 3, 5, 2, 1, 2, 1, 5, 3, 1, 1, 5, 2, 4,
                 4, 2, 3, 5, 1, 4, 2, 3, 1, 2, 1, 4, 2, 3, 2, 5, 1, 4, 2, 3, 2, 1, 4, 2, 1, 3]
    num = int(input('enter your number: '))
    print('population of number {0} in our list is {1}'.format(
        num, number_population(num, test_list)))
