class Solution:
    def prefixSum2D(self, mat, queries):
        n = len(mat)
        m = len(mat[0])
        
        # Build prefix sum matrix
        pre = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                pre[i + 1][j + 1] = (
                    mat[i][j]
                    + pre[i][j + 1]
                    + pre[i + 1][j]
                    - pre[i][j]
                )
        
        ans = []
        for r1, c1, r2, c2 in queries:
            s = (
                pre[r2 + 1][c2 + 1]
                - pre[r1][c2 + 1]
                - pre[r2 + 1][c1]
                + pre[r1][c1]
            )
            ans.append(s)
        
        return ans