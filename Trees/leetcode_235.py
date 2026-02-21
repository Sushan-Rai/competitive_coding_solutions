'''
So here we already know that the tree is a binary search tree and follows the convention
Left < Root < Right
so we can reduce the search space if both the values are not in right or the left subspaces 
if there exists a condition where p and q are in different subtrees then the result becomes the
parent or the current node.
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        if p.val < root.val and q.val < root.val:
            res = self.lowestCommonAncestor(root.left,p,q)
        elif p.val > root.val and q.val > root.val:
            res = self.lowestCommonAncestor(root.right,p,q)
        return res