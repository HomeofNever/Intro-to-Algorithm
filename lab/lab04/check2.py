from pre import *


def median_of_medians(A, i):
    # divide A into sublists of len 5
    sublists = [A[j:j+5] for j in range(0, len(A), 5)]
    medians = [sorted(sublist)[len(sublist)/2] for sublist in sublists]
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)/2]
    else:
        # the pivot is the median of the medians
        pivot = median_of_medians(medians, len(medians)/2)

    # partitioning step
    left = []
    right = []
    same = []
    for j in A:
        if j < pivot:
            left.append(j)
        elif j > pivot:
            right.append(j)
        else:
            same.append(j)

    k = len(left)
    s = len(same)
    if i < k:
        return median_of_medians(left, i)
    elif i > k + s:
        return median_of_medians(right, i-k-s)
    else:
        return same[0]


if __name__ == '__main__':
    print(median_of_medians(test1['ls'], test1['k']) == test1['ans'])
    print(median_of_medians(test2['ls'], test2['k']))
    # Random
    test = randomGenerator(10000)
    print(test)
    print(median_of_medians(test['ls'], test['k']))
