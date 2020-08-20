"""

Egg Dropping Puzzle 
Suppose you have N eggs and you want to determine from which floor in a K-floor building you can drop an egg such that it doesn't break. You have to determine the minimum number of attempts you need in order find the critical floor in the worst case while using the best strategy.There are few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the eggs breaks at a certain floor, it will break at any floor above.


 k ==> Number of floors
  n ==> Number of Eggs
  eggDrop(n, k) ==> Minimum number of trials needed to find the critical
                    floor in worst case.
  eggDrop(n, k) = 1 + min{max(eggDrop(n - 1, x - 1), eggDrop(n, k - x)): 
                 x in {1, 2, ..., k}}
                 
"""

#Python 3
# Function to get minimum number of trials needed in worst
# case with n eggs and k floors
def eggDrop(n, k):
    # A 2D table where entery eggFloor[i][j] will represent minimum
    # number of trials needed for i eggs and j floors.
    eggFloor = [[0 for x in range(k + 1)] for x in range(n + 1)]

    # We need one trial for one floor and0 trials for 0 floors
    for i in range(1, n + 1):
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0

    # We always need j trials for one egg and j floors.
    for j in range(1, k + 1):
        eggFloor[1][j] = j

        # Fill rest of the entries in table using optimal substructure
    # property
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            eggFloor[i][j] = float("inf")
            for x in range(1, j + 1):
                res = 1 + max(eggFloor[i - 1][x - 1], eggFloor[i][j - x])
                if res < eggFloor[i][j]:
                    eggFloor[i][j] = res

                    # eggFloor[n][k] holds the result
    return eggFloor[n][k]
    
    
    
    
    
def eggDrop(n, k):

    
    eggFloor = [[0 for x in range(k+1)] for x in range(n+1)]
    for i in range(1, n+1): 
        eggFloor[i][1] = 1
        eggFloor[i][0] = 0
        
    for j in range(1, k+1): 
        eggFloor[1][j] = j 
    
    for i in range(2, n+1): 
        for j in range(2, k+1): 
            eggFloor[i][j] = sys.maxsize 
            for x in range(1, j+1): 
                res = 1 + max(eggFloor[i-1][x-1], eggFloor[i][j-x]) 
                if res < eggFloor[i][j]: 
                    eggFloor[i][j] = res
                    
    return eggFloor[n][k]
