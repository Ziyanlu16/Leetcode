from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrames = defaultdict(list)

        for str in strs:
            sorted_word = "".join(sorted(str))
            anagrames[sorted_word].append(str)

        return anagrames.values()