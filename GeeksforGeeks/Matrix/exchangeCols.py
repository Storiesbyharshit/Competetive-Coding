#Python 3

def exchangeColumns(matrix):
    n1 = len(matrix)
    m1 = len(matrix[0])
    for i in range(n1): 
        temp=matrix[i][0]
        matrix[i][0]=matrix[i][m1-1]
        matrix[i][m1-1]=temp
