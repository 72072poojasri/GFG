from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        dq = deque()
        res = []

        for i in range(n):
            # Remove indices out of window
            if dq and dq[0] == i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and arr[dq[-1]] < arr[i]:
                dq.pop()

            dq.append(i)

            # Add max when window is complete
            if i >= k - 1:
                res.append(arr[dq[0]])

        return res
