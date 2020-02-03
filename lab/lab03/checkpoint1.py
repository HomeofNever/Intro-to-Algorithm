import random


def init_array(n, p):
    array = []

    # init array
    for i in range(0, n):
        array.append([0] * n)

    for i in range(0, n):
        for j in range(0, n):
            if i != j:
                if array[i][j] != 1:
                    if random.random() <= p:
                        array[i][j] = 1
                        array[j][i] = 1

    return array


def ask_array():
    n = input("Number of specific nodes:")
    n = int(n)
    p = input("Probability: ")
    p = float(p)
    return init_array(n, p)


def print_matrix(array):
    n = len(array)
    print("     ", end="")
    for i in range(0, n):
        print(" {} ".format(i), end="")
    print()
    for i in range(0, n):
        print(" {} : ".format(i), end="")
        for j in range(0, n):
            print(" {} ".format(array[i][j]), end="")
        print()


if __name__ == '__main__':
    # print
    print_matrix(ask_array())
