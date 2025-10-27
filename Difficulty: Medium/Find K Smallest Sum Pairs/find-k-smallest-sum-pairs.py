import heapq

class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        # Edge case: empty arrays
        if not arr1 or not arr2:
            return []
        
        heap = []
        
        # Initialize the heap with first element of arr2 for each arr1 element
        for i in range(min(k, len(arr1))):
            heapq.heappush(heap, (arr1[i] + arr2[0], i, 0))
        
        result = []
        
        while heap and len(result) < k:
            s, i, j = heapq.heappop(heap)
            result.append([arr1[i], arr2[j]])
            
            if j + 1 < len(arr2):
                heapq.heappush(heap, (arr1[i] + arr2[j + 1], i, j + 1))
        
        return result
