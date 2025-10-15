# Definition for a binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        # In-order traversal generator
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.data
                yield from inorder(node.right)
        
        # Iterate over generator to find kth element
        count = 0
        for val in inorder(root):
            count += 1
            if count == k:
                return val
        return -1

# Helper function to build BST from level-order input
def buildTree(s):
    arr = s.strip().split()
    if not arr or arr[0] == 'N':
        return None
    
    root = Node(int(arr[0]))
    queue = [root]
    i = 1
    while queue and i < len(arr):
        curr = queue.pop(0)
        
        # Left child
        if arr[i] != 'N':
            curr.left = Node(int(arr[i]))
            queue.append(curr.left)
        i += 1
        if i >= len(arr):
            break
        
        # Right child
        if arr[i] != 'N':
            curr.right = Node(int(arr[i]))
            queue.append(curr.right)
        i += 1
    return root
