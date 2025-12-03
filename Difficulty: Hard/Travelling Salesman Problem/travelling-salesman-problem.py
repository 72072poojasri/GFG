class Solution:
    def tsp(self, cost):
        n = len(cost)

        # Special case: only 1 city (0 → 0)
        if n == 1:
            return 0

        # dp[mask][i] = minimum cost to visit cities in mask ending at city i
        dp = [[float('inf')] * n for _ in range(1 << n)]
        dp[1][0] = 0  # start at city 0

        for mask in range(1 << n):
            for u in range(n):
                if not (mask & (1 << u)):
                    continue
                if dp[mask][u] == float('inf'):
                    continue

                for v in range(n):
                    if mask & (1 << v):   # v already visited
                        continue
                    new_mask = mask | (1 << v)
                    dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

        final_mask = (1 << n) - 1
        ans = float('inf')

        # return back to city 0
        for i in range(1, n):
            ans = min(ans, dp[final_mask][i] + cost[i][0])

        return ans
