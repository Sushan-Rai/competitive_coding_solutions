# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
So for this problem just traverse till the leaf and then sum up the value
with the string built from the root. the total will be recorded and thus 
the answer. use int(z,2) to convert the given string to binary.'''
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        sum_ = [0]
        def dfs(root,str1):
            if root is None:
                return
            str1 += str(root.val)
            if root.left is None and root.right is None:
                sum_[0] += (int(str1,2))
                return 
            dfs(root.left,str1)
            dfs(root.right,str1)
            return
        dfs(root, "")
        return sum_[0]
        