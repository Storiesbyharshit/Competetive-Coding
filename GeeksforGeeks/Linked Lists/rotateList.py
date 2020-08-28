def rotateList(head, k):
    if k == 0:
        return head
    
    walk = head
    prev = None
    
    for _ in range(k):
    # this loop is run k number of times
    # walk pointer moves k nodes ahead and reaches new head node
        prev = walk
        walk = walk.next
        
        if walk is None:
            return head
    
    newHead = walk
    # since 'prev' points to the node placed before newHead
    # it is new tail, hence prev->next should be NULL
    prev.next = None
    
    while walk.next is not None:
        # walking till the last node
        walk = walk.next
    
    # connecting last node to old head
    walk.next = head
    return newHead
