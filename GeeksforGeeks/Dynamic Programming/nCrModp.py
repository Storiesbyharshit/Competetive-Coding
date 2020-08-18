# A Dynamic Programming based solution to compute nCr % p 
  
# Returns nCr % p 
def nCrModp(n, r, p): 
  
    # Optimization for the cases when r is large 
    # compared to n-r  
    if (r > n- r): 
        r = n - r   
  
    # The array C is going to store last row of 
    # pascal triangle at the end. And last entry 
    # of last row is nCr. 
    C = [0 for i in range(r + 1)] 
  
    C[0] = 1 # Top row of Pascal Triangle 
  
    # One by constructs remaining rows of Pascal 
    # Triangle from top to bottom 
    for i in range(1, n + 1): 
  
        # Fill entries of current row  
        # using previous row values 
        for j in range(min(i, r), 0, -1): 
  
            # nCj = (n - 1)Cj + (n - 1)C(j - 1) 
            C[j] = (C[j] + C[j-1]) % p 
  
    return C[r] 
  
# Driver Program 
n = 10
r = 2
p = 13
print('Value of nCr % p is', nCrModp(n, r, p)) 
