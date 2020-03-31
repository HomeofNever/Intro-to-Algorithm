import random

def precedures(x):
    # allocate space for subproblems
    l = len(x)
    temp = [[[] for x in range(l)] for x in range(l)] 

    # Base case 1: single character
    for i in range(l):
        temp[i][i] = [ x[i] ]
    
    for sub_len in range(2, l + 1):
        for i in range(l - sub_len+ 1):
            j = sub_len + i - 1
            # Base case 2: if there are two character and they are the same
            if  x[i] == x[j] and sub_len == 2:
                temp[i][j] = [x[i], x[j]]
            # Base case 3: first and last are the same 
            elif x[i] == x[j]:
                temp[i][j] = [ x[i] ] +  temp[i + 1][j - 1] + [ x[j] ]
            # Base case 4: the first character and the last character are not the same
            else:
                a = temp[i][j - 1]
                b = temp[i + 1][j]
                temp[i][j] = a if len(a) > len(b) else b

    return temp[0][l - 1]

def randList():
    return [random.randint(1, 100) for i in range(1001)]

if __name__ == '__main__':
    print("Given Test...")
    demo = [9, 14, 9, 5, 10, 6, 15, 6, 13, 9]
    print(precedures(demo))
    hard_code = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
    print(precedures(hard_code))

    # Random
    print("random list test...")
    rlist1 = randList()
    print("Rand list Generated")
    print(precedures(rlist1))

    # average length
    print("Average Length...")
    avg = []
    for i in range(30):
        avg.append(len(precedures(randList())))
    
    print("Avg Length of {} times is {}".format(len(avg), sum(avg) / len(avg)))

    
