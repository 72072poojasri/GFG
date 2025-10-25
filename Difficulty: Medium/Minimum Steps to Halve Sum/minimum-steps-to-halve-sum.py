import heapq

class Solution:
    def minOperations(self, arr):
        total = sum(arr)
        target = total / 2
        heap = [-x for x in arr]  # max heap using negatives
        heapq.heapify(heap)
        
        curr_sum = total
        ops = 0
        
        while curr_sum > target:
            max_val = -heapq.heappop(heap)
            half_val = max_val / 2
            curr_sum -= half_val
            heapq.heappush(heap, -half_val)
            ops += 1
        
        return ops