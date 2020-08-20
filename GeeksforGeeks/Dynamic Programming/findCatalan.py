"""Given a number N. The task is to find the Nth catalan number.
The first few Catalan numbers for N = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
Note: Positions start from 0 as shown above."""


def findCatalan(n): 
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
  
    # Return last entry 
    return catalan[n] 

