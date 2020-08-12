def maxSubArraySum(a,size): 
       
    max_so_far = -9999999 - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i]
        
        # if max_so_far is less than max_ending_here
        # then update max_so_far
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
    
        # check if max_ending_here becomes negative at any point
        # then make it 0
        if max_ending_here < 0: 
            max_ending_here = 0   
    
    return max_so_far
