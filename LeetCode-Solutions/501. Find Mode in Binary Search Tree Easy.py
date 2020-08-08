# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ## Traverse in order and keep track of counts
        counts = {}
        def preorder(node):
            if node: 
                if node.val in counts:
                    counts[node.val] += 1
                else:
                    counts[node.val] = 1
            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)
        preorder(root)
        tot = max(counts.values())      
        return [num for num in counts if counts[num] == tot]
            
