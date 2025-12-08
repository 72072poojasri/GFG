class Solution:
    def matrixChainOrder(self, arr):
        n = len(arr)
        m = [[0] * n for _ in range(n)]
        split = [[0] * n for _ in range(n)]

        # L = chain length
        for L in range(2, n):  
            for i in range(1, n - L + 1):
                j = i + L - 1
                m[i][j] = float('inf')

                for k in range(i, j):
                    cost = m[i][k] + m[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                    if cost < m[i][j]:
                        m[i][j] = cost
                        split[i][j] = k

        # Reconstruct solution string
        return self.build(1, n - 1, split)

    def build(self, i, j, split):
        # Only one matrix → no brackets
        if i == j:
            return chr(ord('A') + i - 1)

        k = split[i][j]
        left = self.build(i, k, split)
        right = self.build(k + 1, j, split)
        return "(" + left + right + ")"
