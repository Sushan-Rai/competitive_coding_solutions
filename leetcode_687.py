# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
so for this problem just go to till the leaf fetch the node value equate it to 0
and then fetch the value towards the parent and check if both the left and the right node
have the same value as the parent if it does take the sum + 2 to include the root path and
forward the bigger path without the divergence i.e. max(left, right), if the left or the right value matches with
the parent then forward it to the parent of the current traversal node record the max value as you do it.'''
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        max_ = [0]
        def dfs(root):
            if root is None:
                return [-1000000,0]
            left = dfs(root.left)
            right = dfs(root.right)
            if left[0] == right[0] and left[0] == root.val:
                res = [root.val, max(left[1],right[1]) + 1]
                max_[0] = max(max_[0], left[1] + right[1] + 2)
            elif left[0] == root.val:
                res = [root.val, left[1] + 1]
                max_[0] = max(max_[0], left[1] + 1)
            elif right[0] == root.val:
                res = [root.val, right[1] + 1]
                max_[0] = max(max_[0], right[1] + 1)
            else:
                res = [root.val, 0]
            return res
        dfs(root)
        return max_[0]
            