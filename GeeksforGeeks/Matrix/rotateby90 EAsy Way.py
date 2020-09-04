def rotateby90(a, n): 
    #Your code here
    
    for r in zip(*a):
        a.append(list(r))
        
    i=0
    j=len(a)-1
    while i<j:
        a[i], a[j] = a[j], a[i]
        i+=1
        j-=1
