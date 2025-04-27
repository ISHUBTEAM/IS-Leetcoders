class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        original = x  
        reversed_num = 0
        
        while x != 0:
            remainder = x % 10
            reversed_num = reversed_num * 10 + remainder
            x //= 10
        
        return original == reversed_num