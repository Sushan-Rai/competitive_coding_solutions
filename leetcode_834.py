'''
for this problem a similar approach can be taken that is take the results from the leaf to the root.
There are 3 different steps to be taken to solve this problem. before we even start with the steps, we
need to build the tree so i created a class with data members being value and children (a list of TreeNodes)
after this we take the adj dictionary to find the neighbours and a simple dfs traversal is created.
assuming we are finding the sum of distances for only the root then we would need the summation of the
children's answer as well as the count of each of the children. this is the frontprop code the second
step, in order to get the count values in O(1) time we use a simple dfs traversal to record the count.
the backprop function is used to propagate the answer of the root to the children in order to find the
sum of distances from the children to the rest of the nodes. the previously evaluated result is used here
wherein the answer of the child is equal to the answer of the parent with the removal of the n connections
(count) of the child to the parent and addition of rest of the nodes not including the connections in the child
(n - count).
'''

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        class TreeNode():
            def __init__(self, val: int):
                self.val = val
                self.children = []
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = [False] * n
        def dfs(val):
            print(val)
            if visited[val] == True:
                return None
            node = TreeNode(val)
            visited[val] = True
            for i in adj[val]:
                node.children.append(dfs(i))
            return node
        root = dfs(0)
        count_ = [0] * n
        def count(root):
            if root is None:
                return 0
            res = 1
            for node in root.children:
                res += count(node)
            count_[root.val] = res
            return res
        count(root)
        ans = [0]*n
        def frontprop(root):
            if root is None:
                return 0
            res = 0
            for node in root.children:
                res += frontprop(node)
                if node is not None:
                    res += count_[node.val]
            ans[root.val] = res
            return res
        frontprop(root)
        def backprop(root):
            if root is None:
                return
            for node in root.children:
                if node is not None:   
                    ans[node.val] = ans[root.val] - count_[node.val] + (n - count_[node.val])
                backprop(node)
            return
        backprop(root)
        return ans