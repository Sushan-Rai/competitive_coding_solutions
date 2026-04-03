# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
This one was a really tricky one to solve since the traversal for this was really confusing
initial approach was to traverse in BFS style or level order style but the placement of the
nodes is the tricky part here. in the problem statement its clearly mentioned that the parent
strictly will have a left node as the child node if it has only one node. so my approach was to
get the levels of all the nodes through a split function and level counter lev, then we can use a
stack variable to move in a dfs style and once the levels are not matching we can come back by 
popping the current depth to reach the desired depth, thus forming a dfs traversal. we store the
node and the depth for each stack object to take reference from.
'''
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        level = []
        lev = 0
        trav = traversal.split("-")
        for i in trav:
            if i == "":
                lev+=1
            else:
                level.append([lev,int(i)])
                lev = 1
        stack = []
        stack.append([level[0][0],TreeNode(level[0][1])])
        i = 1 
        while i < len(level):
            # print(i)
            while stack[-1][0] >= level[i][0]:
                stack.pop(-1)
            # print(level[i])
            ref = TreeNode(level[i][1])
            if stack[-1][1].left is None:
                stack[-1][1].left = ref
            else:
                stack[-1][1].right = ref
            stack.append([level[i][0],ref])
            # print(stack)
            i+=1
        return stack[0][1]
