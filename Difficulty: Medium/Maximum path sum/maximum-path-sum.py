# Definition for a binary tree node.
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def findMaxSum(self, root):
        self.max_sum = float('-inf')
        
        def helper(node):
            if not node:
                return 0
            
            # Max path sum starting from left/right child (ignore negatives)
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)
            
            # Update max_sum if path through current node is bigger
            self.max_sum = max(self.max_sum, node.data + left + right)
            
            # Return max path sum starting from current node to one side
            return node.data + max(left, right)
        
        helper(root)
        return self.max_sum
