# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None :
            return root
        dummy = []
        result = []
        dummy.append(root)
        while len(dummy)>0:
            l = len(dummy)
            ans = []
            for i in range(l):
                node = dummy.pop(0)
                ans.append(node.val)
                if node.left != None:
                    dummy.append(node.left)
                if node.right != None:
                    dummy.append(node.right)
                    
            result.append(ans)
            
        return reversed(result)
            
                
