"""Here, We will use the formula Dividend = Divisor * Quotient + Remainder
where Divisor = max_element
           Quotient = New number at index i after rearrangement
           Remainder = Old Number at index i before rearrangement
           Dividend = The number stored at index i

The even indices store Max elements and the odd indices store Min elements. Traverse the array, and look for elements accordingly, multiply it with Divisor (max_element) and add the value present at arr[i]

Divisor is a value which is higher than values stored in array (in this case n - size of array, as array elements are between 0 to n-1)
Obviously, don't forget to remove the multiplier n from the values while accessing and outputting the new values."""
#Python 3

def rearrange(arr, n): 
  
    # Initialize index of first minimum  
    # and first maximum element 
    max_idx = n - 1
    min_idx = 0
  
    # Store maximum element of array 
    max_elem = arr[n-1] + 1
  
    # Traverse array elements 
    for i in range(0, n) : 
  
        # At even index : we have to put maximum element 
        if i % 2 == 0 : 
            arr[i] += (arr[max_idx] % max_elem ) * max_elem 
            max_idx -= 1
  
        # At odd index : we have to put minimum element 
        else : 
            arr[i] += (arr[min_idx] % max_elem ) * max_elem 
            min_idx += 1
  
    # array elements back to it's original form 
    for i in range(0, n) : 
        arr[i] = arr[i] // max_elem  
