class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        dp = [0] * n

        for i in range(n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]