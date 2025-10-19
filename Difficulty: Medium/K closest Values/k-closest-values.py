class Solution:
    def getKClosest(self, root, target, k):
        def inorder(node):
            return inorder(node.left) + [node.data] + inorder(node.right) if node else []
        arr = inorder(root)
        arr.sort(key=lambda x: (abs(x - target), x))
        return arr[:k]