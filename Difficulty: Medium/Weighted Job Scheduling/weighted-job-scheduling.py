import bisect

class Solution:
    def maxProfit(self, jobs):
        jobs.sort(key=lambda x: x[1])  # sort by end time
        n = len(jobs)

        dp = [0] * (n + 1)
        ends = [job[1] for job in jobs]

        for i in range(1, n + 1):
            start, end, profit = jobs[i - 1]
            # Find the last job that ends <= start
            j = bisect.bisect_right(ends, start) - 1
            dp[i] = max(dp[i - 1], dp[j + 1] + profit)

        return dp[n]