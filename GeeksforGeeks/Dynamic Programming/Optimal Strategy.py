"""

````````````````````````````````
Optimal Strategy For A Game 
````````````````````````````````
You are given an array A of size N. The array contains integers and is of even length.
The elements of the array represent N coin of values V1, V2, ....Vn. You play against an opponent in an alternating way.

In each turn, a player selects either the first or last coin from the row, removes it
from the row permanently, and receives the value of the coin.

You need to determine the maximum possible amount of money you can win if you go first.


F(i, j)  represents the maximum value the user can collect from 
         i'th coin to j'th coin.

    F(i, j)  = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
                   Vj + min(F(i+1, j-1), F(i, j-2) )) 
Base Cases
    F(i, j)  = Vi           If j == i
    F(i, j)  = max(Vi, Vj)  If j == i+1
 """
 
 #Python 3
# Returns optimal value possible that 
# a player can collect from an array  
# of coins of size n. Note than n  
# must be even  
def optimalStrategyOfGame(arr, n):
    '''
    :param arr: given array
    :param n: given size of array
    :return: Integer 
    '''
    # Create a table to store  
    # solutions of subproblems  
    table = [[0 for i in range(n)]
             for i in range(n)]

    # Fill table using above recursive  
    # formula. Note that the table is  
    # filled in diagonal fashion  
    # (similar to http:// goo.gl/PQqoS), 
    # from diagonal elements to 
    # table[0][n-1] which is the result.  
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap

            # Here x is value of F(i+2, j),  
            # y is F(i+1, j-1) and z is  
            # F(i, j-2) in above recursive  
            # formula  
            x = 0
            if ((i + 2) <= j):
                x = table[i + 2][j]
            y = 0
            if ((i + 1) <= (j - 1)):
                y = table[i + 1][j - 1]
            z = 0
            if (i <= (j - 2)):
                z = table[i][j - 2]
            table[i][j] = max(arr[i] + min(x, y),
                              arr[j] + min(y, z))
    return table[0][n - 1]
