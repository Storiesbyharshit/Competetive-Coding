# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        sum = sum - root.val
        
        if not root.left and not root.right and sum == 0 :
            return True
        return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
        
