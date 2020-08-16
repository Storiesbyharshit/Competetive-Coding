Print first n Fibonacci Numbers 
Given a number N, find the first N Fibonacci numbers. The first two number of the series are 1 and 1.





#Python 3

def printFibb(n):
    res = []
    a=b=1
    if n>=1:
        res.append (1)
    if n>=2:
        res.append (1)
        
        
    for i in range(2,n):
        res.append (a+b)
        c=a+b
        a=b
        b=c
    return res
    
  #app2  
    n = int(input())
    if n == 1:
        print("1")
        break
    else:
        a = 1
        b = 1
        print(a, end=" ")
        print(b, end=" ")
        for j in range(n-2):
            c = a + b
            a,b = b,c
            print(c, end=" ")
        print()
        
       
        
