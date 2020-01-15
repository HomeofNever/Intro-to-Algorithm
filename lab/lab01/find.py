import random 

def find_missing(arr):
    n = len(arr) + 1
    sum = (1 + n) * n // 2
    for i in arr:
        sum -= i

    return sum


def gen_arr(length):
    arr = list(range(1, length))
    r1 = random.randint(0, length)
    print("Missing number: {}".format(r1))
    arr.remove(r1)
    print("Find Missing: {}".format(find_missing(arr)))


gen_arr(200)