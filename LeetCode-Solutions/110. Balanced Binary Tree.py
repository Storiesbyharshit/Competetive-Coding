110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def height(root): 
      # base condition when binary tree is empty 
        if root is None: 
            return 0
        
        return max(height(root.left), height(root.right)) + 1

class Solution:

    
    def isBalanced(self, root: TreeNode) -> bool:
        # Base condition 
        if root is None: 
            return True

        # for left and right subtree height 
        lh = height(root.left) 
        rh = height(root.right) 

        # allowed values for (lh - rh) are 1, -1, 0 
        if (abs(lh - rh) <= 1) and self.isBalanced( 
        root.left) is True and self.isBalanced( root.right) is True: 
            return True

        # if we reach here means tree is not  
        # height-balanced tree 
        return False
