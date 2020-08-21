"""
# Try to calculate number of paths for reaching any cell (moves allowed only left, right, top and bottom), 
# starting from 1st cell of the matrix. You will notice that number of paths to reach any cell will depend on two previous states,
# i.e, upper nearest cell from where we can reach current cell and left nearest cell as sum of number of paths to reach these cells.
""
def NumberOfPaths(a, b):
    ans = [[0 for i in range(b)] for j in range(a)]
    for i in range(b):
        ans[0][i]=1
    for i in range(a):
        ans[i][0]=1
    for i in range(1, a):
        for j in range(1, b):
            ans[i][j] = ans[i-1][j]+ans[i][j-1]
    return ans[a-1][b-1]
    
def numberOfPaths(m, n): 
    # Create a 2D table to store 
    # results of subproblems 
    count = [[0 for x in range(m)] for y in range(n)] 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for i in range(m): 
        count[i][0] = 1; 
    
    # Count of paths to reach any  
    # cell in first column is 1 
    for j in range(n): 
        count[0][j] = 1; 
    
    # Calculate count of paths for other 
    # cells in bottom-up  
    # manner using the recursive solution 
    for i in range(1, m): 
        for j in range(1, n):              
            count[i][j] = count[i-1][j] + count[i][j-1] 
    return count[m-1][n-1] 








def numberOfPaths(m, n): 
# If either given row number is first 
# or given column number is first 
    if(m == 1 or n == 1): 
        return 1
  
# If diagonal movements are allowed 
# then the last addition 
# is required. 
    return numberOfPaths(m-1, n) + numberOfPaths(m, n-1) 
