class Solution:
    def sortIt(self, arr):
        odds = []
        evens = []

        for x in arr:
            if x % 2:
                odds.append(x)
            else:
                evens.append(x)

        odds.sort(reverse=True)
        evens.sort()

        arr[:] = odds + evens