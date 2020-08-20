"""
Stickler Thief 
Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule when looting the houses. 
According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize 
the amount he loots. The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy.
He asks for your help to find the maximum money 

can get if he strictly follows the rule. Each house has a[i] amount of money present in it.

Compete Solution:

We will create 4 variables, excl_prev, incl_prev, excl_curr, incl_curr.
excl_prev = it includes sum upto previous element excluding it.
incl_prev = it includes sum upto previous element including it.
excl_curr = it includes sum upto curr element excluding it. = 0
incl_curr = it includes sum upto curr element including it. = arr[0]
Now, iterate from 1 to n-1
excl_curr = max(incl_prev, excl_prev)
incl_curr = excl_prev + arr[i]
excl_prev = exc_curr (for next iteration)
incl_prev = incl_curr (for next iteration)
return max (incl_curr, excl_curr)

"""

#Python 3
# calculate the maximum stolen value
def FindMaxSum(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    if n == 0:
        return 0
    if n == 1:
        return a[0]
    if n == 2:
        return max(a[0], a[1])

    # dp[i] represent the maximum value stolen so
    # for after reaching house i.
    dp = [0] * n

    # Initialize the dp[0] and dp[1]
    dp[0] = a[0]
    dp[1] = max(a[0], a[1])

    # Fill remaining positions
    for i in range(2, n):
        dp[i] = max(a[i] + dp[i - 2], dp[i - 1])

    return dp[-1]
