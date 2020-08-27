def sortedMerge(head_A, head_B):
    # a dummy first node to hang the result on
    dummy = Node(0)
  
    # tail points to the last result node
    tail = dummy

    while head_A is not None and head_B is not None:
        
        if head_A.data <= head_B.data:
            tail.next = head_A
            head_A = head_A.next;
        
        else:
            tail.next = head_B
            head_B = head_B.next
        
        tail = tail.next; 
    
    # inlcuding remaining nodes
    if head_A is None:
        tail.next = head_B
    if head_B is None:
        tail.next = head_A
    
    return dummy.next
