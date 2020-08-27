def getNthfromEnd(head,n):
    # using two pointers, similar to finding middle element
    curr_node = head
    nth_node = head

    while n :
        if n and curr_node == None:
            return -1
        curr_node = curr_node.next
        n-=1

    while curr_node :
        curr_node = curr_node.next
        nth_node = nth_node.next

    return nth_node.data
"""
Another approach is to use two pointers.
Both pointers are initialized to head.

Take a variable count starting from 0. 
First pointers moves forwards (one step each time) till the 
count becomes n-1 from the front. Then the other pointer and 
the first pointer start moving simultaneously. This keeps on
going till the first pointer becomes null. At this point the 
second pointer will be at the desired node.
""" 
