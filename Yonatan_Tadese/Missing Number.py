#3ms
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
        
        
# 2208ms
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        total = len(nums) + 1
        missed = [item for item in range(0, total) if item not in nums]
        return missed[0]
        