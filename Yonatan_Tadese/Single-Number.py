class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = []

        for i in nums:
            if i not in unique:
                unique.append(i)
            else:
                unique.remove(i)
        
        return unique[0]