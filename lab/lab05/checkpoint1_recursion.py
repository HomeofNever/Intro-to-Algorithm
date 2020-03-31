def lps(seq, i, j):
    
    # Base case 1: single character
    if i == j:
        return [ seq[i] ]

    # Base case 2: if there are two character and they are the same
    if (seq[i] == seq [j] and i == j - 1):
        return [ seq[i],  seq[j] ]

    # Base case 3: first and last are the same 
    if (seq[i] == seq[j]):
        return [ seq[i] ] + lps(seq, i + 1, j - 1) + [ seq[j] ]
    else :
        a = lps(seq, i, j - 1)
        b = lps(seq, i + 1, j)  
        return a if len(a) > len(b) else b
    # Base case 4: the first character and the last character are not the same

if __name__ == '__main__':
    demo = [9, 14, 9, 5, 10, 6, 15, 6, 13, 9]
    print(lps(demo, 0, len(demo) - 1))
    hard_code = [7, 2, 4, 6, 9, 11, 2, 6, 10, 6, 15, 6, 14, 2, 7, 5, 13, 9, 12, 15]
    print(lps(hard_code, 0, len(hard_code) - 1))