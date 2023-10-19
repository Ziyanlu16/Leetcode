class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:  # 检查矩阵是否为空
            return []
        ans = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for j in range(left, right+1):
                ans.append(matrix[top][j])
            top += 1

            for k in range(top, bottom+1):
                ans.append(matrix[k][right])
            right -= 1

            if bottom >= top:  # 检查是否还有行需要遍历
                for i in range(right, left-1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            if right >= left:  # 检查是否还有列需要遍历
                for l in range(bottom, top-1, -1):
                    ans.append(matrix[l][left])
                left += 1

        return ans
