'''
Used an array because it retains the content when we use a recursive function
used dfs to traverse and basically get the solution by recording the absolute value of the difference of the subtrees of each node
later check whether the value is greater than 2. could be optimized'''


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        val = [0]
        def func(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return 1
            left_val = func(root.left)
            right_val = func(root.right)
            val[0] = max(val[0], abs(right_val-left_val))
            return max(left_val,right_val) + 1
        res = func(root)
        return True if val[0] < 2 else False

'''
We begin recording the heights of the subtrees and once we get to know that the tree is not balanced with the condition we populate the
value with -1 to the corresponding parents and therefore use that result.''' 
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def postorder(root):
            if not root:
                return 0
            left_height = postorder(root.left)
            right_height = postorder(root.right)

            if abs(left_height - right_height) > 1:
                return -1
            if left_height == -1 or right_height == -1:
                return -1
            return 1 + max(left_height, right_height)
        return postorder(root) != -1