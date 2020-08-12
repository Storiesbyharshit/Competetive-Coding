
#Complete this function
def stockBuySell(A,n):
    i = 0
    if n == 1:
        print("No Profit")
        return
    flag = False
    while(i < n-1):
        while(i < n-1 and A[i] >= A[i+1]):
            i += 1
        if i == n-1:
            break
        buy = i
        i += 1
        while(i < n and A[i] >= A[i-1]):
            i += 1
        sell = i - 1
        print('({} {})'.format(buy,sell), end=' ')
        flag = True
    if flag:
        print('\r')
    else:
        print('No Profit')
    
    
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3


import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            stockBuySell(arr,n)
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
