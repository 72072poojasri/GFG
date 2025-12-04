class Solution:
    def minCost(self, keys, freq):
        n = len(keys)
        
        # Prefix sum for fast frequency range sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + freq[i]
        
        def range_sum(i, j):
            return prefix[j+1] - prefix[i]
        
        # dp[i][j] = optimal cost of BST from keys i..j
        dp = [[0] * n for _ in range(n)]
        
        # Base case: single element tree
        for i in range(n):
            dp[i][i] = freq[i]
        
        # Consider chains of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                total = range_sum(i, j)
                
                # Try each index r as root
                for r in range(i, j + 1):
                    left = dp[i][r - 1] if r > i else 0
                    right = dp[r + 1][j] if r < j else 0
                    dp[i][j] = min(dp[i][j], left + right + total)
        
        return dp[0][n - 1]