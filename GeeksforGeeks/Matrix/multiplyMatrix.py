def multiplyMatrix(A,B):
    n1 = len(A)
    m1 = len(A[0])
    n2 = len(B)
    m2 = len(B[0])
    result = []

    if(m1 == n2):
        result = [[0 for j in range(m2)] for i in range(n1)]
        for i in range(n1):
            for j in range(m2):
                sum = 0
                for k in range(0, m1):  
                    sum += A[i][k] * B[k][j]  
                result[i][j] = sum
    return result
