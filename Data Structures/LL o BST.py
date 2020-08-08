# Python3 implementation of above approach 
  
# Link list node  
class LNode : 
    def __init__(self): 
        self.data = None
        self.next = None
  
# A Binary Tree node  
class TNode : 
    def __init__(self): 
        self.data = None
        self.left = None
        self.right = None
  
head = None
  
# This function counts the number of  
# nodes in Linked List and then calls  
# sortedListToBSTRecur() to construct BST  
def sortedListToBST():  
    global head 
      
    # Count the number of nodes in Linked List  
    n = countLNodes(head)  
  
    # Construct BST  
    return sortedListToBSTRecur(n)  
  
# The main function that constructs  
# balanced BST and returns root of it.  
# head -. Pointer to pointer to  
# head node of linked list n -. No. 
# of nodes in Linked List  
def sortedListToBSTRecur( n) : 
    global head 
      
    # Base Case  
    if (n <= 0) : 
        return None
  
    # Recursively construct the left subtree  
    left = sortedListToBSTRecur( int(n/2))  
  
    # Allocate memory for root, and  
    # link the above constructed left  
    # subtree with root  
    root = newNode((head).data)  
    root.left = left  
  
    # Change head pointer of Linked List 
    # for parent recursive calls  
    head = (head).next
  
    # Recursively construct the right  
    # subtree and link it with root  
    # The number of nodes in right subtree 
    # is total nodes - nodes in  
    # left subtree - 1 (for root) which is n-n/2-1 
    root.right = sortedListToBSTRecur( n - int(n/2) - 1)  
  
    return root  
  
# UTILITY FUNCTIONS  
  
# A utility function that returns  
# count of nodes in a given Linked List  
def countLNodes(head) : 
  
    count = 0
    temp = head  
    while(temp != None):  
      
        temp = temp.next
        count = count + 1
      
    return count  
  
# Function to insert a node  
#at the beginging of the linked list  
def push(head, new_data) : 
  
    # allocate node  
    new_node = LNode() 
      
    # put in the data  
    new_node.data = new_data  
  
    # link the old list off the new node  
    new_node.next = (head)  
  
    # move the head to point to the new node  
    (head) = new_node  
    return head 
  
  
# Function to print nodes in a given linked list  
def printList(node):  
  
    while(node != None):  
      
        print( node.data ,end= " ")  
        node = node.next
      
# Helper function that allocates a new node with the  
# given data and None left and right pointers.  
def newNode(data) : 
  
    node = TNode() 
    node.data = data  
    node.left = None
    node.right = None
  
    return node  
  
# A utility function to  
# print preorder traversal of BST  
def preOrder( node) : 
  
    if (node == None) : 
        return
    print(node.data, end = " " ) 
    preOrder(node.left)  
    preOrder(node.right)  
  
# Driver code 
  
# Start with the empty list  
head = None
  
# Let us create a sorted linked list to test the functions  
# Created linked list will be 1.2.3.4.5.6.7  
head = push(head, 7)  
head = push(head, 6)  
head = push(head, 5)  
head = push(head, 4)  
head = push(head, 3)  
head = push(head, 2)  
head = push(head, 1)  
  
print("Given Linked List " ) 
printList(head)  
  
# Convert List to BST  
root = sortedListToBST()  
print("\nPreOrder Traversal of constructed BST ")  
preOrder(root)  
