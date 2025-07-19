class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new = []

        for i in nums:
            if i < 0:
                new.append((~i + 1) ** 2)
            else:
                new.append(i ** 2)
        new.sort()
        return new
        