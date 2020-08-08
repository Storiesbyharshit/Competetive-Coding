# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root):
        res = []
        def dfs(n, A):
            if n:
                A.append( str(n.val) )
                if (not n.left) and (not n.right):
                    res.append( '->'.join(A) )
                else:
                    dfs(n.left ,A)
                    dfs(n.right,A)
                A.pop()
        dfs(root,[])
        return res        
