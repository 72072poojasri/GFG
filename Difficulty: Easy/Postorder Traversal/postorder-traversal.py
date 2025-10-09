# User function Template for python3

class Solution:
    # Function to return a list containing the postorder traversal of the tree.
    def postOrder(self, root):
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.data)

        dfs(root)
        return res
