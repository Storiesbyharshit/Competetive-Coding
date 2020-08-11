def frequencycount(A,N):
    # code here
    import collections
    freq_dict = collections.Counter(A)
    return freq_dict.values()


def printfrequency(A,N):
    newArr = [0] * N
    for i in range(N):
        newArr[A[i]-1] +=1
    for ele in newArr:
        print(ele, end=" ")
