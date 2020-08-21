"""
Lets discuss the Recursive solution first

Here it is:

Let isSubsetSum(arr, n, sum/2) be the function that returns true if 
there is a subset of arr[0..n-1] with sum equal to sum/2
The isSubsetSum problem can be divided into two subproblems
 a) isSubsetSum() without considering last element 
    (reducing n to n-1)
 b) isSubsetSum considering the last element 
    (reducing sum/2 by arr[n-1] and n to n-1)
If any of the above the above subproblems return true, then return true. 
isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
                              isSubsetSum (arr, n-1, sum/2 - arr[n-1]
                              
                              
                              
Create a bool 2D array  - DP[(sum/2) + 1][n+1] (as the there are 2 state of this DP to consider - sum and numer i.e which element is considered or not)

This array wil tell if the subset with current sum is possible or not.

Fill the first row as true and first column as false (base condition)

Now for complete DP array, do :

dp[i][j] = dp[i][j-1] (to show that current sum is possible if particluar element is included, or it is not )
if i>= arr[j-1], then dp[i][j] = dp[i][j] || dp[i - arr[j-1]][j-1]
Return DP[sum/2][n] , this shows that this sum was possible or not with the given elements


"""
def isSubsetSum(arr, n, sum): 
     
    # The value of subset[i%2][j] will be true  
    # if there exists a subset of sum j in  
    # arr[0, 1, ...., i-1] 
    subset = [ [False for j in range(sum + 1)] for i in range(3) ] 
   
    for i in range(n + 1): 
        for j in range(sum + 1): 
            # A subset with sum 0 is always possible  
            if (j == 0): 
                subset[i % 2][j] = True
   
            # If there exists no element no sum  
            # is possible  
            elif (i == 0): 
                subset[i % 2][j] = False
            elif (arr[i - 1] <= j): 
                subset[i % 2][j] = subset[(i + 1) % 2][j - arr[i - 1]] or subset[(i + 1)  
                                                                               % 2][j] 
            else: 
                subset[i % 2][j] = subset[(i + 1) % 2][j] 
                  
    return subset[n % 2][sum]
  
    
def findPartition(arr,n):
    sm=sum(arr)
    
    if sm%2==0:
        return isSubsetSum(arr, n, sm//2)
    else:
        return
     
     
# Dynamic Programming based python  
# program to partition problem 
  
# Returns true if arr[] can be  
# partitioned in two subsets of  
# equal sum, otherwise false 
def findPartition(arr, n): 
    sum = 0
    i, j = 0, 0
      
    # calculate sum of all elements 
    for i in range(n): 
        sum += arr[i] 
      
    if sum % 2 != 0: 
        return false 
      
    part = [[ True for i in range(n + 1)]  
                   for j in range(sum // 2 + 1)] 
      
    # initialize top row as true 
    for i in range(0, n + 1): 
        part[0][i] = True
          
    # initialize leftmost column,  
    # except part[0][0], as 0 
    for i in range(1, sum // 2 + 1): 
        part[i][0] = False
      
    # fill the partition table in 
    # bottom up manner 
    for i in range(1, sum // 2 + 1): 
          
        for j in range(1, n + 1): 
            part[i][j] = part[i][j - 1] 
              
            if i >= arr[j - 1]: 
                part[i][j] = (part[i][j] or 
                              part[i - arr[j - 1]][j - 1]) 
          
    return part[sum // 2][n]
