

"""
Maximize The Cut Segments 
Given an integer N denoting the Length of a line segment. You need to cut the line segment in such a
way that the cut length of a line segment each time is either x , y or z. Here x, y, and z are integers.

After performing all the cut operations, your total number of cut segments must be maximum.
the problem can be solved by using dynamic programming in O(n) time.Here we should consider all 
segment lengths x,y,z and finding the best out of all cutted segment lengths. 
for the total length of the segment consider the following recurences// for x, y, z running a loop
   
   
 for(int j=0;j<3;j++)
    {
        // updating the point where we can reach from x,y,z
        for(int i=1;i<=n;i++)
        {
            // we will update on if the point is x,y,z or if the 
            // points are visited by some combination of x,y,z.
            if(i==arr[j] or (i>arr[j] and dp[i-arr[j]]>0))
            dp[i]=max(dp[i-arr[j]]+1,dp[i]);
        }
    }

then 
dp[n] gives the final answer.
"""


#Python 3

def maximizeTheCuts( l, p, q, r): 
  
    dp = [-1]*(l + 1)  
  
    dp[0] = 0
  
    for i in range( l+1) : 
  
        if (dp[i] == -1): 
            continue
 
        if (i + p <= l): 
            dp[i + p] = (max(dp[i + p],  
                        dp[i] + 1)) 
  
       
        if (i + q <= l): 
            dp[i + q] = (max(dp[i + q],  
                        dp[i] + 1)) 
  
        
        if (i + r <= l): 
            dp[i + r] = (max(dp[i + r], 
                        dp[i] + 1)) 
  
    if(dp[l]==-1):
        return 0
    return dp[l] 



# Python implementation  
# to divide N into maximum  
# number of segments of  
# length a, b and c 
  
# function to find  
# the maximum number  
# of segments 
def maximumSegments(n, a, b, c) : 
  
    # stores the maximum  
    # number of segments  
    # each index can have 
    dp = [-1] * (n + 10) 
  
    # 0th index will have  
    # 0 segments base case 
    dp[0] = 0
  
    # traverse for all possible 
    # segments till n 
    for i in range(0, n) : 
      
        if (dp[i] != -1) : 
          
            # conditions 
            if(i + a <= n ): # avoid buffer overflow     
                dp[i + a] = max(dp[i] + 1,  
                            dp[i + a]) 
                              
            if(i + b <= n ): # avoid buffer overflow     
                dp[i + b] = max(dp[i] + 1,  
                            dp[i + b]) 
                              
            if(i + c <= n ): # avoid buffer overflow     
                dp[i + c] = max(dp[i] + 1,  
                            dp[i + c]) 
  
    return dp[n]
