class Solution:
    def LCIS(self, a: list, b: list) -> int:
        n, m = len(a), len(b)
        dp = [0] * m
        for i in range(n):
            cur = 0
            for j in range(m):
                if a[i] == b[j]:
                    dp[j] = cur + 1
                elif a[i] > b[j]:
                    if dp[j] > cur:
                        cur = dp[j]
        return max(dp) if dp else 0