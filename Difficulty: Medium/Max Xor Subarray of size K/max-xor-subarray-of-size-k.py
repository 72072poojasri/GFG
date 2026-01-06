class Solution:
    def maxSubarrayXOR(self, arr, k):
        n = len(arr)
        
        # XOR of first window
        curr_xor = 0
        for i in range(k):
            curr_xor ^= arr[i]
        
        max_xor = curr_xor
        
        # Slide the window
        for i in range(k, n):
            curr_xor ^= arr[i - k]  # remove left element
            curr_xor ^= arr[i]      # add right element
            max_xor = max(max_xor, curr_xor)
        
        return max_xor