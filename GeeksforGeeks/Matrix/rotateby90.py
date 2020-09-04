def transpose(matrix,n):
    R,C=n,n
    for i in range(R): 
        for j in range(i, C): 
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
   
# After transpose we swap elements of 
# column one by one for finding left 
# rotation of matrix by 90 degree 
def reverseColumns(matrix,n):
    C=n
    R=n
    for i in range(C): 
        j = 0
        k = C-1
        while j < k: 
            matrix[j][i],matrix[k][i] = matrix[k][i],matrix[j][i]
            j += 1
            k -= 1

# Function to rotate matrix anticlockwise by 90 degree 
def rotateby90(a, n): 
    transpose(a,n) 
    reverseColumns(a,n) 
