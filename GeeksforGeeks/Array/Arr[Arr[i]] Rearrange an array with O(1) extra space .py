def arrange(arr, n): 
    
    # changing the array elements
    # to rearrange
    for i in range(0,n):
        arr[i]+=(arr[arr[i]]%n)*n
        
    # reverting the elements
    for i in range(0,n):
        arr[i]=arr[i]//n
