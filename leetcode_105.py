'''a weird way of solving the problem,
so basically start of with the understanding that
pre-order means root L R
in-order means L R root
so an array consisting of pre-order binary tree will be of the form
[Root left_subtree right_subtree]
and the left subtrees and the right subtrees can be expanded similarly
so the preorder array becomes a reference for the root node
now coming to the inorder array this will be 
[left_subtree Root right_subtree] in order to find the root index
in the inorder array we make use of pre order root and lookup the 
element and subpartition it into left and right subtrees
until we cannot make any partitions. this way we follow the recursion
with base conditions being left is not greater than right and 
preorder root doesnt span out of the length of the array
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_lookup = {}
        in_lookup = {}
        for i in range(len(preorder)):
            pre_lookup[preorder[i]] = i
            in_lookup[inorder[i]] = i
        def func(ele, left_num, right_num):
            print(ele,left_num, right_num)
            if ele >= len(inorder) or left_num > right_num:
                return None
            cur = TreeNode()
            cur.val = preorder[ele]
            right = ele
            for i in range(left_num, in_lookup[cur.val]):
                right = max(right, pre_lookup[inorder[i]])
            cur.left = func(ele+1, left_num, in_lookup[cur.val] - 1)
            cur.right = func(right+1, in_lookup[cur.val]+1, right_num)
            return cur
        return func(0, 0, len(inorder)-1)