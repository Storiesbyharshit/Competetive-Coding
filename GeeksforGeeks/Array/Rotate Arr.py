def rotateArr(A,D,N):
    
    # reverse array from 0 to D
    A[0:D]=reversed(A[0:D])
    
    # reverse array from D to N
    A[D:N]=reversed(A[D:N])
    
    # reverse whole array
    A[0:N]=reversed(A[0:N])
