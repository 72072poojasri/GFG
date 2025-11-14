class Solution:
    def mergeStones(self, stones: list, k: int) -> int:
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stones[i]

        INF = 10**15
        dp = [[0]*n for _ in range(n)]

        for length in range(k, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = INF
                for m in range(i, j, k-1):
                    dp[i][j] = min(dp[i][j], dp[i][m] + dp[m+1][j])
                if (length - 1) % (k - 1) == 0:
                    dp[i][j] += prefix[j+1] - prefix[i]

        return dp[0][n-1]