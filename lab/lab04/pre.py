import random

test1 = {
    'ls': [9, 14, 9, 5, 10, 6, 15, 6, 13, 9],
    'k': 5,
    'ans': 9
}

test2 = {
    'ls': [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15],
    'k': 10
}


def randomGenerator(n=10000000):
    ls = []
    for i in range(n):
        ls.append(random.randint(0, n / 100))

    return {
        'ls': ls,
        'k': n / 2
    }


if __name__ == '__main__':
    print(test1)
    print(test2)
    print(randomGenerator(n=1000))
