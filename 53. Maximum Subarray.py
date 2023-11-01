class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        current_sum = 0

        for i in range(len(nums)):
            current_sum += nums[i] #update
            current_sum = max(current_sum + nums[i], nums[i])
            
            max_sum = max(max_sum, current_sum)

        return max_sum