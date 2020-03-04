from pre import *


def randomizeFind(ls, k):
    # Init list
    left = []
    right = []
    same = []

    # Pick a random number from the list
    num = random.choice(ls)

    # Compare
    for i in ls:
        if i > num:
            right.append(i)
        elif i < num:
            left.append(i)
        else:
            same.append(num)

    # Identify list
    if k < len(left):
        return randomizeFind(left, k)
    elif k < len(left) + len(same):
        return same[0]
    else:
        return randomizeFind(right, k - len(left) - len(same))


if __name__ == '__main__':
    print(randomizeFind(test1['ls'], test1['k']) == test1['ans'])
    print(randomizeFind(test2['ls'], test2['k']))
    # Random
    test = randomGenerator(10000)
    print(test)
    print(randomizeFind(test['ls'], test['k']))
