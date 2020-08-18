Count number of hops 
A frog jumps either 1, 2, or 3 steps to go to the top. In how many ways can it reach the top. As the answer will be large find the answer modulo 1000000007.

def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    mod = 1000000007
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
        
    a = 1
    b = 2
    c = 4
    
    for i in range (4, n+1):
        temp = (a + b + c) % mod
        a,b,c = b,c,temp
        
    return c
