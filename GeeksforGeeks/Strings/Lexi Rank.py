"""
1.

Let the given string be “STRING”. In the input string, ‘S’ is the first character. There are total 6 characters and 4 of them are smaller than ‘S’. So there can be 4 * 5! smaller strings where first character is smaller than ‘S’, like following

R X X X X X
I X X X X X
N X X X X X
G X X X X X

Now let us Fix S’ and find the smaller strings staring with ‘S’.

Repeat the same process for T, rank is 4*5! + 4*4! +…

Now fix T and repeat the same process for R, rank is 4*5! + 4*4! + 3*3! +…

Now fix R and repeat the same process for I, rank is 4*5! + 4*4! + 3*3! + 1*2! +…

Now fix I and repeat the same process for N, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! +…

Now fix N and repeat the same process for G, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0!

Rank = 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0! = 597

Note that the above computations find count of smaller strings. Therefore rank of given string is count of smaller strings plus 1. The final rank = 1 + 597 = 598

"""

def findRank(s):
    Ispresent=[0 for i in range(256)] #boolean to mark visited characters

    for char in s:
        if(Ispresent[ord(char)]):
            return 0
        else:
            Ispresent[ord(char)]=1
            
    rank=0 # current rank of string initialized to 0.

    for i in range(len(s)):
        less=sum(Ispresent[:ord(s[i])])
        rank += (get_fact(len(s) - i - 1) * less) % 1000000007
        Ispresent[ord(s[i])]-=1
    return rank+1
    
#returns factorial modulo 1000000007.
def get_fact(n):
    if(n==0):
        return 0
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact%1000000007




