#Fibonacci Numbers - Top Down DP 
One of the rudimentary problems to understand DP is finding the nth Fibonacci number. Here, we will solve the problem using the top-down approach.

You are given a number N. You need to find Nth Fibonacci number. The first two term of the series are 1 and 1.


#User function Template for python3
##Complete this function
dp=[0]*100

def findNthFibonacci(number):
   
    if(dp[number]>0):
        return dp[number]
    else:
        if number == 1 or number == 0:
            dp[number] = number
        else:
            dp[number] = findNthFibonacci(number-1) + findNthFibonacci(number-2) 
    ##Complete this line. dp[number] is equal to function(n-1)+function(n-2)
    return dp[number]
    

def findNthFibonacci(number):
   
    if(dp[number]>0):
        return dp[number]
    ##Complete this line. dp[number] is equal to function(n-1)+function(n-2)
    dp[number] = findNthFibonacci(number-1) + findNthFibonacci(number-2)
    return dp[number]


##Complete this function
def findNthFibonacci(number, dp):
    # Your Code Here
    l=[]
    l.append(0)
    l.append(1)
    for i in range(2,number+1):
        l.append(l[i-1]+l[i-2])
    return l[number]
    
  
  




    
    
def memoize(f):
    memo = {}
    def helper(x,y):
        if x not in memo:            
            memo[x] = f(x,y)
        return memo[x]
    return helper
    
@memoize
def findNthFibonacci(number, dp):
    if(number<2): return number
    else: return findNthFibonacci(number-1,dp)+findNthFibonacci(number-2,dp)

 
