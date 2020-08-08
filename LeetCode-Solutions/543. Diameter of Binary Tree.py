#543. Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def height(node):
            if node is  None:
                return 0
            else:
                return 1+max(height(node.left),height(node.right))
        
        
        def diameter(root):
            
            if root is None:
                return 0
            
            lheight = height(root.left)
            rheight = height(root.right)

            ldia = diameter(root.left)
            rdia = diameter(root.right)

            return max(lheight+rheight,max(ldia,rdia)) #edges = n-1
        #print (lheight,rheight,ldia,rdia)
        
        return diameter(root)
