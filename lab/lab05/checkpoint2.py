
# add the item with the highest value/weight ratio within the overall budget W constraint.
def greedy(x, w):
    d = {}
    # Calculate all ratios
    for i in x:
        ratio = i[1] / i[0]
        if d.get(ratio) is None:
            d[ratio] = []
        
        d[ratio].append(i)
    
    temp = 0
    accepted = []
    s = 0
    # Loop through by ratios
    for i in sorted(d.keys(), reverse=True):
        for j in d[i]:
            if temp + j[0] <= w:
                temp += j[0]
                accepted.append(j)
                s += j[1]

    return temp, accepted, s

def dp(x, w):
    n = len(x)
    # Base Case 1: The current length of the list or the current testing weight is 0
    table = [[0 for i in range(w + 1)]for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, w + 1):
            # Base Case 2: The current weight/value pair can be added to current testing weight
            if x[i - 1][0] <= j:
                table[i][j] = max(x[i - 1][1] + table[i - 1][w - x[i - 1][0]], table[i - 1][w])
            # Base Case 3, The current weight is out of current testing weight
            else:
                table[i][j] = table[i - 1][j]

    return table[n][w]

if __name__ == '__main__':
    hard_code =  [[96, 91], [96, 92], [96, 92], [97, 94], [98, 95], [100, 94], [100, 96], [102, 97], [103, 97], 
                                 [104, 99], [106, 101], [107, 101], [106, 102], [107, 102], [109, 104], [109, 106], [110, 107], [111, 108],[113, 107], [114, 110]]
    w = [100, 200, 300]
    print ("test greedy")
    for i in w: 
        print("w={}, result: {}".format(i, greedy(hard_code, i)))

    print("test dp")
    for i in w: 
        print("w={}, result: {}".format(i, dp(hard_code, i)))
