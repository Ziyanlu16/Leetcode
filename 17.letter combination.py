class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}  # 键为字符串
        
        ans = []
        if digits == '':
            return []

        def backtracking(temp_combination, index):
            if len(temp_combination) == len(digits):
                ans.append(temp_combination)
                return

            if index < len(digits):
                current_digit = digits[index]  # 获取当前数字字符
                letters = dic[current_digit]  # 从字典中获取字母字符串

                for letter in letters:  # 遍历字母字符串的每个字符
                    backtracking(temp_combination+letter, index+1) 
        
        backtracking('', 0)
        return ans
