def arrayReversal(arr,sizeOfArr):
    for i in range(0,sizeOfArr//2): #running the loop till half distance 
        temp=arr[i]
        arr[i]=arr[sizeOfArr-1-i]
        arr[sizeOfArr-1-i]=temp #we swap the elements like 1st with last and so on
