class Solution:
    def countLessEqual(self, arr, x):
        n = len(arr)

        # Find pivot (minimum element index)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        pivot = low

        # Binary search to count <= x in a sorted range
        def count_leq(start, end):
            l, r = start, end
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] <= x:
                    l = mid + 1
                else:
                    r = mid - 1
            return r - start + 1

        count = 0
        if pivot > 0:
            count += count_leq(0, pivot - 1)
        count += count_leq(pivot, n - 1)

        return count
