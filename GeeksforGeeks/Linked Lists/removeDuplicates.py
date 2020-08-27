def removeDuplicates(head):
    curr_node=head
    while curr_node.next:
        if(curr_node.data == curr_node.next.data):
            curr_node.next = curr_node.next.next
        else:
            curr_node=curr_node.next
