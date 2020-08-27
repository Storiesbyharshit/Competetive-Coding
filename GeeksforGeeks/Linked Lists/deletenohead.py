def deleteNode(curr_node):
    # handle case with empty or single element
    if curr_node is None:
        return
    
    if curr_node.next is None: 
        curr_node.data = None
        return

    elif curr_node.next.next is None:
        curr_node.data=curr_node.next.data
        curr_node.next=None
        return

    curr_node.data = curr_node.next.data
    deleteNode(curr_node.next)


"""
It would be a simple deletion problem from the singly linked list 
if the head pointer was given because for deletion you must know 
the previous node and you can easily reach there by traversing from the head pointer. 


Conventional deletion is impossible without knowledge of the previous node of a node which needs to be deleted.

The trick here is we can copy the data of the next node to the data field 
of the current node to be deleted. Then we can move one step forward.
Now our next has become the current node and current has become the previous node.
Now we can easily delete the current node by conventional deletion methods.
"""
