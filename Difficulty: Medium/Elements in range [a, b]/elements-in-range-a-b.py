from bisect import bisect_left, bisect_right

class Solution:
    def cntInRange(self, arr, queries):
        arr.sort()
        res = []
        
        for a, b in queries:
            left = bisect_left(arr, a)
            right = bisect_right(arr, b)
            res.append(right - left)
        
        return res