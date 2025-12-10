class Solution:
    def findTwoElement(self, arr):
        n = len(arr)

        S = sum(arr)
        SS = sum(x * x for x in arr)

        S_exp = n * (n + 1) // 2
        SS_exp = n * (n + 1) * (2 * n + 1) // 6

        diff = S - S_exp              # x - y (repeating - missing)
        diff_sq = SS - SS_exp         # x^2 - y^2 = (x - y)(x + y)

        sum_xy = diff_sq // diff      # x + y

        x = (diff + sum_xy) // 2      # repeating number
        y = x - diff                  # missing number

        return [x, y]