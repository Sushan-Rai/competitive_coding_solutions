# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
u take pairs of values to evaluate two cases for each node
with root and without root so that u decide to include or
not include the node for the base case we give [0,0] to add up
0s and in other cases we for with root we add the root value
with the left subtrees without root and right subtrees without root
since it has a link and then for without root we do not care of the
values coming so we take the max of left subtree and right subtree
and then get the pair. in the end we take the max in the root answer.
'''
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return [0,0]
            pair_left = dfs(root.left)
            pair_right = dfs(root.right)
            with_root = root.val + pair_left[1] + pair_right[1]
            without_root = max(pair_left) + max(pair_right)
            return [with_root,without_root]
        return max(dfs(root))