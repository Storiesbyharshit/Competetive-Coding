def superSeq(X, Y, m, n): 
    if (not m): return n 
    if (not n): return m 
  
    if (X[m - 1] == Y[n - 1]) :  
       return 1 + superSeq(X, Y, m - 1, n - 1) 
  
    return 1 + min(superSeq(X, Y, m - 1, n), 
                superSeq(X, Y, m, n - 1)) 
                
                
 # Function to find length of the 
# shortest supersequence of X and Y. 
def shortestSuperSequence(X, Y): 
    m = len(X) 
    n = len(Y) 
    l = lcs(X, Y, m, n) 
      
    # Result is sum of input string 
    # lengths - length of lcs 
    return (m + n - l) 
