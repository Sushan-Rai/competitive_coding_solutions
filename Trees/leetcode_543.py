# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
For this problem standard take the base condition to be 0
record max values for every node traversal thinking the node has access
to both the left and right subtrees and return the max of the subtrees for 
evaluation of the maximum for the other parent nodes.'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = [0]
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            maxi[0] = max(maxi[0],1+left+right)
            return 1 + max(left,right)
        dfs(root)
        return maxi[0] - 1 if maxi[0]>0 else 0