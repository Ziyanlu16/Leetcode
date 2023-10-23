class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left_bound = right_bound = mid
                while left_bound > 0 and nums[left_bound - 1] == nums[mid]:
                    left_bound -= 1
                while right_bound < len(nums) - 1 and nums[right_bound + 1] == nums[mid]:
                    right_bound += 1

                return [left_bound, right_bound]
            
        return [-1, -1]