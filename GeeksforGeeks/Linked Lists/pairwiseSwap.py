def pairwiseSwap(head):
    
    if head.next is None: #base case with single element
        return head
        
    curr_node=head

    head=curr_node.next # new head after the swaps take place
    while curr_node and curr_node.next :
        temp=curr_node.next.next
        curr_node.next.next=curr_node
        if temp and temp.next:       # if more than one nodes are still left
            curr_node.next=temp.next
        else:
            curr_node.next=temp
        curr_node=temp

    return head
