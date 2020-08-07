class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
  
  
# Recursive function pritn left view of a binary tree 
def leftViewUtil(root, level, max_level): 
      
    # Base Case 
    if root is None: 
        return
  
    # If this is the first node of its level 
    if (max_level[0] < level): 
        print "% d\t" %(root.data), 
        max_level[0] = level 
  
    # Recur for left and right subtree 
    leftViewUtil(root.left, level + 1, max_level) 
    leftViewUtil(root.right, level + 1, max_level) 
  
  
# A wrapper over leftViewUtil() 
def leftView(root): 
    max_level = [0] 
    leftViewUtil(root, 1, max_level) 
    
# Recursive function to print right view of Binary Tree 
# used max_level as reference list ..only max_level[0]  
# is helpful to us 
def rightViewUtil(root, level, max_level): 
      
    # Base Case 
    if root is None: 
        return
      
    # If this is the last node of its level 
    if (max_level[0] < level): 
        print "%d   " %(root.data), 
        max_level[0] = level 
  
    # Recur for right subtree first, then left subtree 
    rightViewUtil(root.right, level+1, max_level) 
    rightViewUtil(root.left, level+1, max_level) 
  
def rightView(root): 
    max_level = [0] 
    rightViewUtil(root, 1, max_level) 
