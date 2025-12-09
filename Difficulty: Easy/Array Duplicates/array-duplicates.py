class Solution:
    def findDuplicates(self, arr):
        res = []
        n = len(arr)

        for i in range(n):
            idx = abs(arr[i]) - 1  # convert value to index

            # If already negative, this index was visited before → duplicate
            if arr[idx] < 0:
                res.append(idx + 1)
            else:
                arr[idx] = -arr[idx]  # mark as visited

        return res
