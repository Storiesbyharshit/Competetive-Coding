def getCount(head_node):
    #code here
    node = head_node
    count = 0
    while node:
        count +=1
        node = node.next
    return count


