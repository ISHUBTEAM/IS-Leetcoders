class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = list(map(lambda x: x, nums))
        for i in nums:
            ans.append(i)
        return ans
        