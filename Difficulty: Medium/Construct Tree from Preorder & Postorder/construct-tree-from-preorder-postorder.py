# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def constructTree(self, pre, post):
        self.pre = pre
        self.post = post
        self.post_index = {val: idx for idx, val in enumerate(post)}
        self.preIndex = 0
        return self.helper(0, len(post) - 1)

    def helper(self, postL, postR):
        if self.preIndex >= len(self.pre) or postL > postR:
            return None

        root_val = self.pre[self.preIndex]
        root = Node(root_val)
        self.preIndex += 1

        if postL == postR:
            return root

        next_val = self.pre[self.preIndex]
        idx = self.post_index[next_val]

        root.left = self.helper(postL, idx)
        root.right = self.helper(idx + 1, postR - 1)
        return root
