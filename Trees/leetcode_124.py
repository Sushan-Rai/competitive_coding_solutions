'''
So here the main problem is to consider the DP approach since the
problem asks for the maximum path and has a overlapping sub problems
of taking the max we need to consider the leaf node. In the leaf node
we can see that the left and right subtree should return values 0 so 
base case and then we can take that particular node as the root and check
if the path has maximum value and take the max while returning we consider 
only a path since it returns for the left or the right subtree max values 
respectively.
'''

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxi = [-1000000]
        def dp(root):
            if root is None:
                return 0
            left = max(0,dp(root.left))
            right = max(0,dp(root.right))
            # print(left,right,root.val)
            maxi[0] = max(maxi[0], root.val + left + right)
            return root.val + max(left,right)
        dp(root)
        return maxi[0]