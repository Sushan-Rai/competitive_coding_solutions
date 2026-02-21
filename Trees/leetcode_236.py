# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
always return to the root
and mainly here dfs once we get one of the elements return it to the parent
and if left has a value and right doesnt then take the left val
if right and left have a value then return parent
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def func(root):
            if root is None:
                return None
            if root.val == p.val:
                return p
            if root.val == q.val:
                return q
            left = func(root.left)
            right = func(root.right)
            if left is None:
                return right
            if right is None:
                return left
            return root
        return func(root)