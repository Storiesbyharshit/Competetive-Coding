Reach a given score 
Consider a game where a player can score 3 or 5 or 10 points in a move. Given a total score n, find the number of distinct combinations to reach the given score.

#Python 3

def count(n): 
  
    table = [0 for i in range(n+1)] 
    table[0] = 1
  
    for i in range(3, n+1): 
        table[i] += table[i-3] 
    for i in range(5, n+1): 
        table[i] += table[i-5] 
    for i in range(10, n+1): 
        table[i] += table[i-10] 
  
    return table[n] 
