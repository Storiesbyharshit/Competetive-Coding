#User function Template for python3
'''
    Your task is to insert a new node in 
	the middle of the linked list with
	the given value.
	
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	
	Function Arguments: head (head of linked list), node (node to be inserted in middle)
	Return Type: None, just insert the new node at mid.
'''
def insertInMid(head,new_node):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    new_node.next = slow.next
    slow.next = new_node

