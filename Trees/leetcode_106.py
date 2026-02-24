# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
so for postorder instead of finding the right we find the left and we go from the end since root is there
like before inorder is L subtree root R subtree and postorder L subtree R subtree Root
so the last node has to be the root and previous one to it is the right subtree parent node.
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_lookup = {}
        post_lookup = {}
        for i in range(len(inorder)):
            in_lookup[inorder[i]] = i
            post_lookup[postorder[i]] = i
        def dfs(idx, minval, maxval):
            if idx < 0 or minval > maxval:
                return None
            root = TreeNode()
            root.val = postorder[idx]
            partition = in_lookup[root.val]
            right = idx - (maxval - partition)
            root.left = dfs(right-1,minval, partition - 1)
            root.right = dfs(idx-1, partition + 1, maxval)
            return root
        return dfs(len(postorder)-1,0,len(inorder)-1)
        