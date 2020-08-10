# Function to find largest and second largest element in the array
def largestAndSecondLargest(sizeOfArray, arr):
    maximum = -1
    second_maximum = -1
    
    '''
    iterating through the array and comparing the elements
    to find max and second max
    '''
    for i in range(0, sizeOfArray):
    
        if arr[i] > maximum:
            second_maximum = maximum
            maximum = arr[i]
            
        elif arr[i] > second_maximum and arr[i] != maximum:
            second_maximum = arr[i]
            
            
    
    ans = [maximum, second_maximum]
    return ans
