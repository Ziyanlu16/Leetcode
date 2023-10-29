class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # 创建一个栈
        mapping = {')': '(', '}': '{', ']': '['}  # 用于匹配括号
        
        for char in s:
            if char in mapping:  # 如果字符是关闭括号
                top_element = stack.pop() if stack else '#'  # 弹出栈顶元素，如果栈为空，则弹出'#'
                
                if mapping[char] != top_element:  # 如果弹出的元素与当前字符不匹配
                    return False
            else:
                stack.append(char)  # 如果字符是开放括号，将其推入栈中
                
        return not stack  # 如果栈为空，返回 True，否则返回 False


