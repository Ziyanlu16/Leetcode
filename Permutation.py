class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtr(start, path):
            if len(path) == k:
                output.append(path[:])
                return
            for i in range(start, n+1):
                path.append(i)
                backtr(i+1, path)
                path.pop()
        output = []
        backtr(1, [])
        return output

print(Solution.combine(0,3,3))