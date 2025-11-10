class Solution:
    def maxProfit(self, arr):
        if not arr:
            return 0

        hold = -arr[0]
        sold = 0
        rest = 0

        for price in arr[1:]:
            prev_hold = hold
            hold = max(hold, rest - price)
            rest = max(rest, sold)
            sold = prev_hold + price

        return max(sold, rest)