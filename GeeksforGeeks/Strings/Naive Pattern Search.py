#Python 3

'''Function to search pattern in the given string
   p: pattern given in input
   s: string given in the input'''
def search(p,s):
    m=len(p)
    n=len(s)
    for i in range(n-m+1):
        j=0
        while(j<m):
            if(s[i+j]!=p[j]):
                break
            j+=1
        if(j==m):
            return True
    return False
