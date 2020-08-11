
def convertToWave(A,N):
    i=0
    
    # swapping the elements to convert the array into wave array
    while(i<N-1):
        temp=A[i]
        A[i]=A[i+1]
        A[i+1]=temp
        i+=2
