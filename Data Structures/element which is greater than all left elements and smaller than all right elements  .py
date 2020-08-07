# Python3 program to find the element which is greater than  
# all left elements and smaller than all right elements.  
  
def findElement(arr, n):  
   
    # leftMax[i] stores maximum of arr[0..i-1]  
    leftMax = [None] * n  
    leftMax[0] = float('-inf')  
  
    # Fill leftMax[]1..n-1]  
    for i in range(1, n):  
        leftMax[i] = max(leftMax[i-1], arr[i-1])  
  
    # Initialize minimum from right  
    rightMin = float('inf')  
  
    # Traverse array from right  
    for i in range(n-1, -1, -1):  
       
        # Check if we found a required element  
        if leftMax[i] < arr[i] and rightMin > arr[i]:  
            return i  
  
        # Update right minimum  
        rightMin = min(rightMin, arr[i])  
       
    # If there was no element matching criteria  
    return -1 
  
