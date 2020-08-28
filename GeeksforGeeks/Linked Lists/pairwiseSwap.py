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

# swap pairwise nodes of the linked list and return the head
def pairwiseSwap(head):
    curr, prev, c = head, None, 2
    while c > 0 and curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode
        c-=1
    if nextNode is not None:
        head.next = pairwiseSwap(nextNode)
    return prev
    
 # swap pairwise nodes of the linked list and return the head
def pairwiseSwap(head):
    #code here
    curr=head
    while curr!=None and curr.next!=None:
        curr.data,curr.next.data=curr.next.data,curr.data
        curr=curr.next.next
    return head
