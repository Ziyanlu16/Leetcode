class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = float('-inf')
        current_sum = 0
        total_sum = 0
        min_sum = float('inf')
        min_current_sum = 0

        for num in nums:
            total_sum += num

            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

            min_current_sum = min(num, min_current_sum + num)
            min_sum = min(min_sum, min_current_sum)

        if max_sum < 0:
            return max_sum
        else:
            return max(max_sum, total_sum - min_sum)