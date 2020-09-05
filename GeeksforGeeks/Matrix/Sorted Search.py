def search(matrix, n, m, x): 
	i, j = n - 1, 0 				
	while (i >= 0 and j < m): 
		if (matrix[i][j] == x): 
			return True; 
		if (matrix[i][j] > x): 
			i -= 1
		else: 
			j += 1
	return False
	
