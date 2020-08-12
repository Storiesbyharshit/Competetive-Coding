def missingNumber(arr,n):#Our original array 
  
    m = max(arr) #Storing maximum value 
    if m < 1: 
          
        # In case all values in our array are negative 
        return 1 
    if n == 1: 
          
        #If it contains only one element 
        return 2 if arr[0] == 1 else 1     
    l = [0] * m 
    for i in range(n): 
        if arr[i] > 0: 
            if l[arr[i] - 1] != 1: 
                  
                #Changing the value status at the index of our list 
                l[arr[i] - 1] = 1 
    for i in range(len(l)): 
          
        #Encountering first 0, i.e, the element with least value 
        if l[i] == 0:  
            return i+1
            #In case all values are filled between 1 and m 
    return i+2 
