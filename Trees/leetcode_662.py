# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
for this problem take the indices into consideration 
we know that parent -> n left->2*n right->2*n+1 if we consider to start at 1
now after this we use bfs and use level order traversal
this helps us create a min and max variable for the indices and then find the difference
between them + 1 will give width in that level we can do this iteratively until we
reach the end and return the max result.
'''
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi = 0
        q = []
        q.append([root,1])
        while len(q) > 0:
            q_ = []
            maxq = 0
            minq = float('inf')
            for cur, idx in q:
                if cur.left is not None:
                    q_.append([cur.left,2*idx])
                if cur.right is not None:
                    q_.append([cur.right,2*idx+1])
                if maxq < idx:
                    maxq = idx
                if minq > idx:
                    minq = idx
            maxi = max(maxi, maxq - minq + 1)
            q = q_
        return maxi