def interchangeRows(n1, m1, arr1):
    low, high = 0, n1 - 1
    while low < high:
        for i in range(m1):
            arr1[low][i], arr1[high][i] = arr1[high][i], arr1[low][i]
        low += 1
        high -= 1
    return
