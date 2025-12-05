class Solution:
    def minCost(self, costs):
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])

        if k == 0:
            return -1
        if n >= 2 and k == 1:
            return -1

        # Initialize dp with first row
        dp = costs[0][:]

        # Find initial min1, min2, idx1
        min1 = min2 = float('inf')
        idx1 = -1

        for c in range(k):
            if dp[c] < min1:
                min2 = min1
                min1 = dp[c]
                idx1 = c
            elif dp[c] < min2:
                min2 = dp[c]

        # Process rows 1..n-1
        for i in range(1, n):
            new_dp = [0] * k
            new_min1 = new_min2 = float('inf')
            new_idx1 = -1

            for c in range(k):
                if c == idx1:
                    new_dp[c] = costs[i][c] + min2
                else:
                    new_dp[c] = costs[i][c] + min1

                # Update new min1/min2
                if new_dp[c] < new_min1:
                    new_min2 = new_min1
                    new_min1 = new_dp[c]
                    new_idx1 = c
                elif new_dp[c] < new_min2:
                    new_min2 = new_dp[c]

            dp = new_dp
            min1, min2, idx1 = new_min1, new_min2, new_idx1

        return min1