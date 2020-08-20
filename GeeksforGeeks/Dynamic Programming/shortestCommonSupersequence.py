#Python 3
"""
Length of Shortest Common Supersequence = ( Length of str1 + Length of str2 ) - Length of Longest Common Subsequence
"""

def shortestCommonSupersequence(X, Y, m, n): 
    L = [[0] * (n + 2) for i in
                    range(m + 2)] 
      
    for i in range(m + 1): 
          
        for j in range(n + 1): 
              
            if (i == 0):
                L[i][j] = j
            elif (j == 0):
                L[i][j] = i
            elif (X[i - 1] == Y[j - 1]) : 
                L[i][j] = L[i - 1][j - 1] + 1
                  
            else :
                L[i][j] = 1 + min(L[i - 1][j], L[i][j - 1]) 
              
    return L[m][n] 
