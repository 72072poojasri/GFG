# Definition for a binary tree node (as usually provided in GFG/LeetCode)
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    def zigZagTraversal(self, root):
        if not root:
            return []
        
        from collections import deque
        
        result = []
        queue = deque([root])
        left_to_right = True  # direction flag
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.data)
                
                # enqueue children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # reverse level if needed
            if not left_to_right:
                level_nodes.reverse()
            
            result.extend(level_nodes)
            left_to_right = not left_to_right  # flip direction
        
        return result
