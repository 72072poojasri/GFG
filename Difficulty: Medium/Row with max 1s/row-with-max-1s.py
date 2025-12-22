class Solution:
    def rowWithMax1s(self, arr):
        n = len(arr)
        m = len(arr[0])
        
        max_ones = 0
        ans = -1
        
        for i in range(n):
            row = arr[i]
            
            # Binary search for first 1
            left, right = 0, m - 1
            first_one = m
            
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    first_one = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            ones = m - first_one
            
            if ones > max_ones:
                max_ones = ones
                ans = i
        
        return ans