class Solution:
    class TrieNode:
        def __init__(self):        # FIXED init
            self.child = [None, None]
            self.count = 0

    def cntPairs(self, arr, k):
        root = self.TrieNode()

        def insert(num):
            node = root
            for bit in range(15, -1, -1):
                b = (num >> bit) & 1
                if not node.child[b]:
                    node.child[b] = self.TrieNode()
                node = node.child[b]
                node.count += 1

        def query(num, limit):
            node = root
            res = 0
            for bit in range(15, -1, -1):
                if not node:
                    break

                b = (num >> bit) & 1
                kbit = (limit >> bit) & 1

                if kbit == 1:
                    if node.child[b]:
                        res += node.child[b].count
                    node = node.child[1 - b]
                else:
                    node = node.child[b]

            return res

        ans = 0
        for x in arr:
            ans += query(x, k)
            insert(x)

        return ans
