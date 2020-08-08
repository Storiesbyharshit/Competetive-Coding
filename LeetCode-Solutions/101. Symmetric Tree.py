101. Symmetric Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root:
            return True
        
        left=root.left
        right=root.right
        
        if not left and not right:
            return True
        
        def check(t1, t2):
            if not t1 and not t2:
                return True
            if t1 and not t2:
                return False
            if not t1 and t2:
                return False
            if t1.val!=t2.val:
                return False
            return check(t1.left, t2.right) and check(t1.right, t2.left)
        
        return check(left, right)
