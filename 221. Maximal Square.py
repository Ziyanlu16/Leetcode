class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        max_side = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i > 0 and j > 0:
                        dp[i][j]  = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    else:
                        dp[i][j] = 1
                    max_side = max(max_side, dp[i][j])
        
        return max_side**2