# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
so first sum up from the root and then till the leaf then check if the sum is equal to 
the target sum and if its true keep on ORring the result.
'''
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum_(root,summed):
            if root is None:
                return False
            summed += root.val
            if root.left is None and root.right is None:
                return summed == targetSum
            return sum_(root.left,summed) or sum_(root.right,summed)
        return sum_(root,0)