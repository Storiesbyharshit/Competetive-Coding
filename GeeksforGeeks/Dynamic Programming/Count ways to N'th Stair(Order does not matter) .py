There are N stairs, and a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does not matter).
Note: Order does not matter means for n=4 {1 2 1},{2 1 1},{1 1 2} are considered same.

def countWays(m):
    '''
    :param n: given value of n
    :return: Integer , ways to write n as sum of positive integers
    '''
    mod = 1000000007
    dp = [0 for i in range(m+1)]
    dp[0] = 1 # staying on bottom
    dp[1] = 1 # one way to reach stair 1

    for i in range(2,m+1):
        dp[i]=(dp[i-2]%mod+1)%mod

    return dp[m]
