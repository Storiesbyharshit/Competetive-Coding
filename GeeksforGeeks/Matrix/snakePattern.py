def snakePattern(matrix): 
    n = len(matrix)
    output = []

    # Traverse through all rows 
    for i in range(n): 
          
        # If current row is even, 
        # print from left to right 
        if i % 2 == 0: 
            for j in range(n): 
                output.append(matrix[i][j])
  
        # If current row is odd, 
        # print from right to left 
        else: 
            for j in range(n-1, -1, -1): 
                output.append(matrix[i][j])

    return output
