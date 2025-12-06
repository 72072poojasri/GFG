class Solution:
    def maximumAmount(self, arr):
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        # Base case: length 1
        for i in range(n):
            dp[i][i] = arr[i]

        # Fill DP for lengths from 2 to n
        for length in range(2, n + 1):
            for i in range(0, n - length + 1):
                j = i + length - 1

                # Required subproblems
                a = dp[i+2][j] if i + 2 <= j else 0
                b = dp[i+1][j-1] if i + 1 <= j - 1 else 0
                c = dp[i][j-2] if i <= j - 2 else 0

                pick_left = arr[i] + min(a, b)
                pick_right = arr[j] + min(b, c)

                dp[i][j] = pick_left if pick_left > pick_right else pick_right

        return dp[0][n-1]
