class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + ((right - left) // 2)
            if nums[mid] > nums[mid + 1]:
                right = mid

            else:
                left = mid + 1

        return left

print(Solution.findPeakElement(0, [1,3,2,4,5,7,3,1]))