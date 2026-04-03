# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Basic way of using BFS and using each level in the queue and appending to the lst
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def func(root):
            queue = []
            lst = []
            if root is None:
                return lst
            queue.append(root)
            while len(queue) != 0:
                queue_ = []
                lst1 = []
                for ele in queue:
                    lst1.append(ele.val)
                    if ele.left != None:
                        queue_.append(ele.left)
                    if ele.right != None:
                        queue_.append(ele.right)
                lst.append(lst1)
                queue = queue_
            return lst
        return func(root)
    

# OR
'''
Use of a variable val to keep track of the depth and then later using the hashmap to create the res
'''

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        x = {}
        def preorder(root,val):
            if root is None:
                return
            if root.left is None and root.right is None:
                if x.get(val) is None:
                    x[val] = [root.val]
                else:
                    x[val].append(root.val)
                return
            if x.get(val) is None:
                x[val] = [root.val]
            else:
                x[val].append(root.val)
            if root.left is not None:
                preorder(root.left,val+1)
            if root.right is not None:
                preorder(root.right,val+1)
        preorder(root,1)
        res = []
        for i,j in x.items():
            res.append(j)
        return res