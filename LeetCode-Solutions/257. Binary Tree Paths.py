# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_paths(root,path):
            if root:
                path+=str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path+='->'
                    if root.left:
                        construct_paths(root.left,path)
                    if root.right:
                        construct_paths(root.right,path)
        paths=[]
        construct_paths(root,'')
        return paths
    
    
    
    
    
    
    
    
    
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
