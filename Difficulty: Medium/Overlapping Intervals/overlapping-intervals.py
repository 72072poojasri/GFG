class Solution:
    def mergeOverlap(self, arr):
        if not arr:
            return []

        arr.sort(key=lambda x: x[0])
        merged = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i][0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], arr[i][1])
            else:
                merged.append(arr[i])

        return merged