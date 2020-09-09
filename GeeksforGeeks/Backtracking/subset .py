def funcUtil(a,result,start,temp):
    result.append(temp[:]) # add current num in subset
    for i in range(start, len(a)):
        temp.append(a[i])
        funcUtil(a,result,i+1,temp)
        temp.pop() # backtrack for this value

def func(a):
    '''
    :param a: given list a
    :return: print all subsets of a, newline is provided by driver code
    '''

    a.sort()
    result = [] # stores all subsets

    funcUtil(a,result,0,[]) # generate all subsets

    result.sort() # sort the lists

    for i in range(len(result)):
        if(result[i]==result[i-1]): # duplicate subset is skipped
            continue
        print("(",end="")
        size = len(result[i])
        for j in range(size-1):
            print(result[i][j],end=" ")
        if(size):
            print(result[i][size-1],end=")")
        else:
            print(")",end="")

////////////////////////////////////////


def subsetsHelper (arr, i, n, cur, res):
    if i >= n:
        res.append (cur[:])
        return
    
    curInd = i + 1
    while curInd < n and arr[curInd] == arr[i]:
        curInd += 1
        
    count = curInd - i 
    for j in range (0, count+1):
        for k in range (j):
            cur.append (arr[i])
            
        subsetsHelper (arr, curInd, n, cur, res)
        for k in range (j):
            cur.pop ()

def AllSubsets (arr, n):
    res = []
    cur = []
    arr.sort()
    
    subsetsHelper (arr, 0, n, cur, res)
    
    res.sort ()
    return res

