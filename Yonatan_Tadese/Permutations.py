from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        per = permutations(nums)
        res = []

        for i in list(per):
            res.append(i)
            

        return res
        