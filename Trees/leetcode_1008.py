# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
used an index as reference for preorder and constraints for inorder 
and taking information from one another we can build the tree.
inorder of a bst is a sorted nums.
'''
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        in_lookup = {}
        pre_lookup = {}
        for i in range(len(inorder)):
            in_lookup[inorder[i]] = i
            pre_lookup[preorder[i]] = i
        def dfs(idx, minval, maxval):
            if idx >= len(preorder) or minval > maxval:
                return None
            root = TreeNode()
            root.val = preorder[idx]
            partition = in_lookup[root.val]
            root.left = dfs(idx+1 ,minval, partition - 1)
            right = idx + 1 + partition - minval
            root.right = dfs(right ,partition + 1, maxval)
            return root
        return dfs(0, 0, len(inorder))