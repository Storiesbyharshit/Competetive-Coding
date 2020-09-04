"""
Given a boolean matrix of size RxC where each cell contains either 0 or 1,
modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.
"""

#Python 3

def booleanMatrix(matrix):
    R = len(matrix)
    C = len(matrix[0])
    row = [0] * R  
    col = [0] * C  

    for i in range(0, R) :         
        for j in range(0, C) : 
            if (matrix[i][j] == 1) : 
                row[i] = 1
                col[j] = 1
              
    for i in range(0, R) : 
        for j in range(0, C): 
            if ( row[i] == 1 or col[j] == 1 ) : 
                matrix[i][j] = 1


def booleanMatrix(r, c, mat):
    #Your code here
    row = set()
    col = set()
    for i in range(r):
        for j in range(c):
            if(mat[i][j] == 1): 
                row.add(i)
                col.add(j)
    for i in row:
        for j in range(c):
            mat[i][j] = 1
            
    for i in col:
        for j in range(r):
            mat[j][i] = 1
    
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end = ' ')
        print('')    
