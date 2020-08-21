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
