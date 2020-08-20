##

#Python 3
def sumSubstrings(s):
    '''
    :param s: given string s, representing a number
    :return: Integer
    '''
    n = len(s) # length of string
    digits = [] # contains digits
    # converts string into list of digits
    for char in s:
        digits.append(int(char))

    dp = [0 for i in range(n)] # dp[i] represents sum of all substrings generated from digits of 0 to i.

    dp[0] = digits[0] # initialize, sum including first digit
    res = dp[0]  #initialize result
    for i in range(1,n): # iterate from 1 to n-1
        dp[i] = ((i+1)*digits[i]+(dp[i-1]*10))%1000000007 # Get the current digit* (i+1) and add it to dp[i-1]*10
        res+=dp[i] # add value to result
        res%=1000000007;

    return res
    
"""
We can write summation of all substrings on basis of digit at which they are ending in that case,
Sum of all substrings = sumofdigit[0] + sumofdigit[1] + sumofdigit[2] … + sumofdigit[n-1]  where n is length of string.

Where sumofdigit[i] stores sum of all substring ending at ith index digit, in above example,

Example : num = "1234"
sumofdigit[0] = 1 = 1
sumofdigit[1] = 2 + 12  = 14
sumofdigit[2] = 3 + 23  + 123 = 149
sumofdigit[3] = 4 + 34  + 234 + 1234  = 1506
Result = 1670
Now we can get the relation between sumofdigit values and can solve the question iteratively. Each sumofdigit can be represented in terms of previous value as shown below,

For above example,
sumofdigit[3] = 4 + 34 + 234 + 1234
           = 4 + 30 + 4 + 230 + 4 + 1230 + 4
           = 4*4 + 10*(3 + 23 +123)
           = 4*4 + 10*(sumofdigit[2])
In general, 
sumofdigit[i]  =  (i+1)*num[i] + 10*sumofdigit[i-1]
Using above relation we can solve the problem in linear time. 

"""
