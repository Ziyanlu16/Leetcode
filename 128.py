class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hp = set(nums)
        max_lenth = 0

        for num in nums:
            if num-1 not in hp:
                current_len = 1
                current_num = num

                while current_num+1 in hp:
                    current_len += 1
                    current_num += 1
                
                max_lenth = max(max_lenth, current_len)
        return max_lenth