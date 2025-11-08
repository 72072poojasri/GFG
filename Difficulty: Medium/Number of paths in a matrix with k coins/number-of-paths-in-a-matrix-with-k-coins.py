class Solution:
    def numberOfPath(self, mat, k):
        n, m = len(mat), len(mat[0])
        dp = [[[-1 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]

        def solve(i, j, curr_sum):
            if i >= n or j >= m:
                return 0
            curr_sum += mat[i][j]
            if curr_sum > k:
                return 0
            if i == n - 1 and j == m - 1:
                return 1 if curr_sum == k else 0

            if dp[i][j][curr_sum] != -1:
                return dp[i][j][curr_sum]

            down = solve(i + 1, j, curr_sum)
            right = solve(i, j + 1, curr_sum)
            dp[i][j][curr_sum] = down + right
            return dp[i][j][curr_sum]

        return solve(0, 0, 0)