# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
so here what i have done is take copies of path and pass it down and then take the original path and add it up if it matches
the targetSum.
'''
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        lst = []
        def func(root,summed, path):
            if root is None:
                return
            summed += root.val
            path.append(root.val)
            if root.left is None and root.right is None:
                if summed == targetSum:
                    lst.append(path[:])
                return
            func(root.left,summed, path[:])
            func(root.right,summed, path[:])
        func(root,0,[])
        return lst
        