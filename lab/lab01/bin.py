def binary_search(arr, target):
    high = len(arr) - 1
    low = 0

    while low < high:
        index = ( high - low ) // 2 + low
        if arr[index] == target:
            return True
        elif arr[index] < target:
            low = index + 1
        else:
            high = index - 1
    
    return False


target = 101
array = range(0, 100)

print(binary_search(array, target))