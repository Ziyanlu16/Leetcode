class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle) - 2
        for i in range(n, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(triangle[i][j] + triangle[i + 1][j], triangle[i][j] + triangle[i + 1][j+1])

        return triangle[0][0]