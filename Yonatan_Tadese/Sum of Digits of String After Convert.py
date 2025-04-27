class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = ""
        for i in s:
            nums += str(ord(i) - 96)      
        
        for _ in range(k):
            c = 0
            for x in nums:
                c += int(x)
            nums = str(c)

        return int(nums)
        