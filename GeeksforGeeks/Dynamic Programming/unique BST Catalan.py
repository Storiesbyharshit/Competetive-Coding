"""Total number of possible Binary Search Trees with n different keys (countBST(n)) = Catalan number Cn = (2n)!/(n+1)!*n!

For n = 0, 1, 2, 3, … values of Catalan numbers are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …. So are numbers of Binary Search Trees.

Total number of possible Binary Trees with n different keys (countBT(n)) = countBST(n) * n!

 
Unique BST's 
Given an integer. Find how many structurally unique binary search trees are there that stores the values from 1 to that integer (inclusive). u
"""





def numTrees(n):  
  
    # DP to store the number of unique 
    # BST with key i  
    dp = [0] * (n + 1)  
  
    # Base case  
    dp[0], dp[1] = 1, 1
  
    # fill the dp table in top-down  
    # approach.  
    for i in range(2, n + 1):  
        for j in range(1, i + 1):  
  
            # n-i in right * i-1 in left  
            dp[i] = dp[i] + (dp[i - j] * dp[j - 1])  
            if( dp[i] >= 1000000007 ):
                dp[i] = dp[i] % 1000000007
    return dp[n]  
   
# Return the total number of BSTs possible with keys [1....N] inclusive.
def numTrees(n):
    if (n == 0 or n == 1): 
        return 1
  
    # Table to store results of subproblems 
    catalan = [0 for i in range(n + 1)] 
  
    # Initialize first two values in table 
    catalan[0] = 1
    catalan[1] = 1
  
    # Fill entries in catalan[] using recursive formula 
    for i in range(2, n + 1): 
        catalan[i] = 0
        for j in range(i): 
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1] 
            if( catalan[i] >= 1000000007 ):
                catalan[i] = catalan[i] % 1000000007
  
    # Return last entry 
    return catalan[n] 
