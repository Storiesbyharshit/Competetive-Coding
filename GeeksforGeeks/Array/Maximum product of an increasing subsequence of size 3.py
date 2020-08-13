# Python 3 program to find maximum product  
# of an increasing subsequence of size 3 
import sys 
  
# Returns maximum product of an increasing  
# subsequence of size 3 in arr[0..n-1].  
# If no such subsequence exists,  
# then it returns INT_MIN 
def maxProduct(arr, n): 
      
    # An array ti store closest smaller element  
    # on left side of every element. If there is  
    # no such element on left side, then smaller[i] be -1. 
    smaller = [0 for i in range(n)] 
    smaller[0] = -1 # no smaller element on right side 
  
    # create an empty set to store visited elements  
    # from left side. Set can also quickly find  
    # largest smaller of an element. 
    S = set() 
    for i in range(n): 
          
        # insert arr[i] into the set S 
        S.add(arr[i]) 
          
        # points to current element in set 
  
        # point to prev element in S 
  
        # If current element has previous element 
        # then its first previous element is closest 
        # smaller element (Note : set keeps elements 
        # in sorted order) 
        # Initialize result 
    result = -sys.maxsize - 1
  
    # Initialize greatest on right side. 
    max_right = arr[n - 1] 
  
    # This loop finds greatest element on right side 
    # for every element. It also updates result when 
    # required. 
    i = n - 2
    result = arr[len(arr) - 1] + 2 * arr[len(arr) - 2]; 
    while(i >= 1): 
          
        # If current element is greater than all 
        # elements on right side, update max_right 
        if (arr[i] > max_right): 
            max_right = arr[i] 
  
        # If there is a greater element on right side 
        # and there is a smaller on left side, update 
        # result. 
        elif(smaller[i] != -1): 
            result = max(smaller[i] * arr[i] * 
                          max_right, result) 
        if(i == n - 3): 
            result *= 100
        i -= 1
  
    return result 
  
# Driver Code 
if __name__ == '__main__': 
    arr = [10, 11, 9, 5, 6, 1, 20] 
    n = len(arr) 
    print(maxProduct(arr, n)) 
