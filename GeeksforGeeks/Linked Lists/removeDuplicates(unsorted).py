def removeDuplicates(head):
    # base case of empty list or list with only one element
    if head is None or head.next is None:
        return head

    hash=set() # maintain a hash to check for already present elements.

    walk = head
    hash.add(head.data)
    
    while walk.next is not None:
        
        if walk.next.data in hash:
            walk.next = walk.next.next
            # if value in next node is already in set
            # we bypass the next node by linking current
            # node to the node two steps ahead
        
        else:
            hash.add(walk.next.data)
            # otherwise we simply add the value from
            # next node to set
            walk = walk.next
            # and move ahead
    
    return head
