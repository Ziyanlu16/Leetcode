class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_t = {}
        t_s = {}
        for i in range(len(s)):
            if s[i] not in s_t and t[i] not in t_s:
                s_t[s[i]] = t[i]
                t_s[t[i]] = s[i]
            elif s[i] in s_t and s_t[s[i]] == t[i] and t[i] in t_s and t_s[t[i]] == s[i]:
                continue
            else:
                return False
        return True