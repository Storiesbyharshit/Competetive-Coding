# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.arr=[]
        def findleft(root):
            if not root :
                return
            if root.left and root.left.left is None and root.left.right is None :
                self.arr.append(root.left.val)
            findleft(root.left)
            findleft(root.right)
        findleft(root)
        #print (self.arr)
        return (sum(self.arr))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        total = 0
        
        def helper(node, lr):
            nonlocal total
			# Return if we don't have a node.
            if not node: return
			# If we're at a leaf.
            if not node.left and not node.right:
			    # And we're on the left.
                if lr == 'l':
				    # Add the left leaf val to our total.
                    total += node.val
                    return
				# We went to a right leaf.
                return 
			# Traverse left and right subtrees.
            helper(node.left, 'l')
            helper(node.right, 'r')
            
        helper(root, '')
        return total
