#Python 3
def sumUtil(a,n,s,result,temp,index):
    if(index>=n or s<0): # if we have exceeded sum,or no more element is left
        return

    if(s==0): # if we reached the given sum
        result.append(temp[:])
        return

    temp.append(a[index]) # append current element in our temp result
    sumUtil(a,n,s-temp[-1],result,temp,index) # recurse for lesser sum, with curr index
    temp.pop() # pop last element added to temp for backtrack

    sumUtil(a,n,s,result,temp,index+1) # recurse for next position




def combinationalSum(a,s):
    '''
    :param a: given array a
    :param n: size of a
    :param s: given sum to be achieved
    :return: list containing list of numbers in ascending order, giving the combinational sum
    '''
    a=set(a) # put it in set
    a=list(a) # removed duplicates from array a.

    a.sort() # sort to maintain order
    result = []
    sumUtil(a,len(a),s,result,[],0) # initial index is 0
    return result # return result
