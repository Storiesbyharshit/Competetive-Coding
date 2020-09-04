def BoundaryTraversal(matrix, n, m):
    output = []
    if(n == 1):
        i = 0;
        while i < m:
            output.append(matrix[0][i])
            i+=1
    elif(m == 1):
        i = 0;
        while i < n:
            output.append(matrix[i][0])
            i+=1
    else:
        #traversing first row
        row_ind = 0
        col_ind = 0
        while col_ind < m:
            output.append(matrix[row_ind][col_ind])
            col_ind+=1

        # traversing last column
        col_ind = m-1
        row_ind += 1
        while row_ind < n:
            output.append(matrix[row_ind][col_ind])
            row_ind += 1

        # traversing last row
        row_ind = n-1
        col_ind -= 1
        while col_ind > -1:
            output.append(matrix[row_ind][col_ind])
            col_ind -= 1

        # traversing first column
        col_ind = 0
        row_ind -= 1
        while row_ind > 0:
            output.append(matrix[row_ind][col_ind])
            row_ind -= 1

    return output
    
######
######
######
######

def BoundaryTraversal(a,n,m):
    if n == 1:
        for i in range(m):
            print(a[0][i], end=" ")
    elif m == 1:
        for i in range(n):
            print(a[i][0], end=" ")
    else:
        for i in range(m):
            print(a[0][i], end=" ")
        for i in range(1, n):
            print(a[i][m-1], end=" ")
        for i in range(m-2, -1, -1):
            print(a[n-1][i], end=" ")
        for i in range(n-2, 0, -1):
            print(a[i][0], end=" ")
    return
