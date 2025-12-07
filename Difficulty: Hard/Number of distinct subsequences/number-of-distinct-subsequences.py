class Solution:
    def distinctSubseq(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1   # empty subsequence

        last = {}   # last occurrence index

        for i in range(1, n + 1):
            ch = s[i - 1]
            dp[i] = (2 * dp[i - 1]) % MOD

            if ch in last:
                dp[i] = (dp[i] - dp[last[ch] - 1]) % MOD

            last[ch] = i

        return dp[n]