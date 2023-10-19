class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        left = [1] * len(nums)
                
        right = [1] * len(nums)

        temp = 1
        temp2 = 1
        for i in range(len(nums)):
            left[i] = temp
            temp = temp *nums[i]

        for i in range(len(nums) - 1,-1, -1):
            right[i] = temp2
            temp2 *= nums[i]
        
        for j in range(len(nums)):
            left[j] = left[j] * right[j]
        
        return left
        

                