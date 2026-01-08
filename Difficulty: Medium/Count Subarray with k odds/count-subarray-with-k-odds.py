class Solution:
    def countSubarrays(self, arr, k):
        from collections import defaultdict
        cnt = defaultdict(int)
        cnt[0] = 1
        odd = 0
        ans = 0
        for x in arr:
            if x % 2 == 1:
                odd += 1
            if odd - k in cnt:
                ans += cnt[odd - k]
            cnt[odd] += 1
        return ans