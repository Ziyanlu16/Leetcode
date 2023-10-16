class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def sqr(n):
            sum = 0
            while True:
                digit = n % 10
                sum += digit**2
                n = n//10
                if n == 0:
                    break
            return sum
    
        slow = sqr(n)
        fast = sqr(sqr(n))
        while True:
            slow = sqr(slow)
            fast = sqr(sqr(fast))
            if slow == fast != 1:
                return False
            elif slow == fast == 1:
                break
        return True