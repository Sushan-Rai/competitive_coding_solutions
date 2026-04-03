# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
ok so for this problem i used - and = to store value and position in the tree
and then deserialized it using split and a hashmap which will create the tree accordingly.
'''

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        str1 = [""]
        def dfs(root,val):
            if root is None:
                return
            str1[0] += str(val) + "-" + str(root.val) + "="
            dfs(root.left, 2 * val)
            dfs(root.right, 2 * val + 1)
            return
        dfs(root, 1)
        print(str1)
        return str1[0]

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        lst1 = data.split("=")[:-1]
        dict1 = {}
        for i in range(len(lst1)):
            lst1[i] = lst1[i].split("-")
            dict1[int(lst1[i][0])] = int(lst1[i][1])
        if lst1 == []:
            return
        root = None
        def createTree(root, val):
            if dict1.get(val) is not None:
                root = TreeNode()
                root.val = dict1[val]
                root.left = createTree(root.left, 2*val) 
                root.right = createTree(root.left, 2*val + 1) 
                return root
            return None
        return createTree(root, 1)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans