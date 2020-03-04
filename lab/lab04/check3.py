from pre import *


def partition(A, L, H):
    P = random.randint(L, H)
    pivot = A[P]
    left = L
    right = L
    upper_bound = H

    while right <= upper_bound:
        if A[right] < pivot:
            A[left], A[right] = A[right], A[left]
            left += 1
            right += 1
        elif A[right] > pivot:
            A[upper_bound], A[right] = A[right], A[upper_bound]
            upper_bound -= 1
        else:
            right += 1

    return left, right


def quickSort(A, L, H):
    if L < H:
        left, right = partition(A, L, H)

        quickSort(A, L, left - 1)
        quickSort(A, right, H)


def quickSortFind(A, i):
    arr = A.copy()
    quickSort(arr, 0, len(A) - 1)

    return arr[i]


if __name__ == '__main__':
    print(quickSortFind(test1['ls'], test1['k']) == test1['ans'])
    print(quickSortFind(test2['ls'], test2['k']))
    # Random
    # test = randomGenerator(10000)
    # print(test)
    # print(quickSortFind(test['ls'], test['k']))
