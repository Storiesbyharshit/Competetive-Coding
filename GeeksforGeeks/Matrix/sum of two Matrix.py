
def sumMatrix(A,B):
    n1 = len(A)
    m1 = len(A[0])
    n2 = len(B)
    m2 = len(B[0])
    result = []
    if(n1 == n2 and m1 == m2):
        result = [[0 for j in range(m1)] for i in range(n1)]
        for i in range(n1):
            for j in range(m1):
                result[i][j]=A[i][j]+B[i][j]
    return result
