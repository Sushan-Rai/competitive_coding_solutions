# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
for this encode the value and the position using * and = and then use split and a hashmap to get the reference
and place accordingly.
'''

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        str1 = [""]
        def dfs(root,val):
            if root is None:
                return
            str1[0] += str(val) + "*" + str(root.val) + "="
            dfs(root.left, 2 * val)
            dfs(root.right, 2 * val + 1)
            return
        dfs(root, 1)
        print(str1)
        return str1[0]
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst1 = data.split("=")[:-1]
        dict1 = {}
        for i in range(len(lst1)):
            lst1[i] = lst1[i].split("*")
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
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))