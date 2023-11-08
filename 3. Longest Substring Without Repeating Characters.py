class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = 0 #Two pointers
        hashmap = {}
        max_length = 0
        for right in range(len(s)):
            if s[right] in hashmap:
                left = max(left, hashmap[s[right]] + 1)

            hashmap[s[right]] = right
            
            max_length = max(max_length, (right - left + 1))

        return max_length