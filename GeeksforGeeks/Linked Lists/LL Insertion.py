'''

	Function Arguments: a (linked list) and value (value to be inserted)
	Return Type: None
'''
'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
# function should insert new node at the
# beigning of the list
def insertAtBegining(a,value):
    newnode=Node(value)
    newnode.next=a.head
    a.head=newnode
    
# function should insert new node at the
# end of the list
def insertAtEnd(a,value):
    newnode=Node(value)
    temp=a.head
    if temp is None:
        a.head=newnode
        return
    while temp.next:
        temp=temp.next
    temp.next=newnode


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#linked list class
class LinkedList:
    def __init__(self):
        self.head=None

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=LinkedList()
        nodes_info=list(map(int,input().strip().split()))
        for i in range(0,len(nodes_info)-1,2):
            if(nodes_info[i+1]==0):
                insertAtBegining(a,nodes_info[i])
            else:
                insertAtEnd(a,nodes_info[i])
        a.printList()
