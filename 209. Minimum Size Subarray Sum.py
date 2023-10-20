class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left, window_sum = 0, 0
        length = float('inf')
        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                length = min((right-left+1), length)
                window_sum -= nums[left]
                left+=1

        return length if length != float('inf') else 0        

