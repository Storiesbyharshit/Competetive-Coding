def countWays(n):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''

    a = 1
    b = 1
    mod = 1000000007
    
    for i in range (2, n+1):
        temp = (a + b) % mod
        a = b
        b = temp
        
    return b
