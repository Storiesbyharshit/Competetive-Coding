def sumTriangles(matrix, n):
    upper = 0 # upper triangle sum
    lower = 0 # lower triangle sum 
    for i in range(n):
        for j in range(n):
            # The diagonal will be common 
            # to both upper sum and lower sum
            if(i == j):
                upper += matrix[i][j];
                lower += matrix[i][j];
                
            # condition for upper triangle
            elif (j>i):
                upper += matrix[i][j]; 

            # condition for lower triangle
            elif(j<i):
                lower += matrix[i][j]; 

    return [upper,lower]
