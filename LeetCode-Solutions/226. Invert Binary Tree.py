# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return root
        
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        
        root.left = right
        root.right = left
        
        return root
        
 class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = (
                self.invertTree(root.right), 
                self.invertTree(root.left))
        return root
        
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root == None:
            return None
        
        queue = []
        queue.append(root)
        
        while queue:
            s = queue.pop(0)
            if s.left:
                queue.append(s.left)
            if s.right:
                queue.append(s.right)
            s.left, s.right = s.right, s.left
        
        return root
