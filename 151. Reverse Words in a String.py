class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return ' '.join(words)



print(Solution.reverseWords(1,"  hello world  "))