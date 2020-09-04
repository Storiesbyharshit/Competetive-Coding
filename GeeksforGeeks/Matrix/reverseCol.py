def reverseCol(n1, m1, arr1):
    #Your code here
    for i in range(n1):
        arr1[i] = arr1[i][::-1]
        
def reverseCol(n1, m1, arr1):
    low, high = 0, m1-1
    while low < high:
        for i in range(n1):
            arr1[i][low], arr1[i][high] = arr1[i][high], arr1[i][low]
        low += 1
        high -= 1
    return
