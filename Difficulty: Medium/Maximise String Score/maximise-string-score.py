class Solution:
    def maxScore(self, s, jumps):
        n = len(s)
        asc = [ord(ch) for ch in s]

        # build allow table: allow[u][v] True if char u -> char v allowed
        allow = [[False]*26 for _ in range(26)]
        for a, b in jumps:
            allow[ord(a)-97][ord(b)-97] = True

        # prefix sums P and Pc (per character)
        P = [0]*(n+1)
        Pc = [[0]*(n+1) for _ in range(26)]
        for i in range(n):
            P[i+1] = P[i] + asc[i]
            ci = ord(s[i]) - 97
            for c in range(26):
                Pc[c][i+1] = Pc[c][i]
            Pc[ci][i+1] += asc[i]

        NEG = -10**30
        dp = [NEG]*n
        # best[t] = max over seen i of (dp[i] - P[i] + Pc[t][i]) for which s[i] -> t allowed (or same char)
        best = [NEG]*26

        # start at index 0
        dp[0] = 0
        si0 = ord(s[0]) - 97
        # update best for all targets t that s[0] can jump to (including same char)
        for t in range(26):
            if allow[si0][t] or t == si0:
                best[t] = max(best[t], dp[0] - P[0] + Pc[t][0])  # Pc[t][0]==0, P[0]==0

        # process indices 1..n-1
        for j in range(1, n):
            tj = ord(s[j]) - 97
            # compute dp[j] using best for target = tj
            if best[tj] != NEG:
                dp[j] = best[tj] + (P[j] - Pc[tj][j])
            # after computing dp[j], update best[*] for future indices using s[j] as source
            sj = ord(s[j]) - 97
            for t in range(26):
                if allow[sj][t] or t == sj:
                    # dp[j] might be NEG (unreachable); that's fine: best stays unchanged
                    val = dp[j] - P[j] + Pc[t][j]
                    if val > best[t]:
                        best[t] = val

        return max(dp)