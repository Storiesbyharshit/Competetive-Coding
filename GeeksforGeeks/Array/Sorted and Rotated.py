#User function Template for python3

def II (arr, n):
    i = 0 
    while (i < n-1 and arr[i] <= arr[i+1]):
        i += 1
    
    if i == n-1:
        return False
        
    i += 1
    
    while (i < n-1 and arr[i] <= arr[i+1]):
        i += 1

    if (i == n-1 and arr[n-1] <= arr[0]):
        return True
    else:
        return False
        

def DD (arr, n):
    i = 0 
    while (i < n-1 and arr[i] >= arr[i+1]):
        i += 1
    
    if i == n-1:
        return False
        
    i += 1
    
    while (i < n-1 and arr[i] >= arr[i+1]):
        i += 1

    if (i == n-1 and arr[n-1] >= arr[0]):
        return True
    else:
        return False

def checkRotatedAndSorted (arr, n):
    if II (arr,n) == True:
        return True
        
    if DD (arr,n) == True:
        return True
        
    return False
