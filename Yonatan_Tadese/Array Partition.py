class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        sum = 0
        arr = []

        for i in range(0, len(nums), 2):
            arr.append(i)
        
        for j in arr:
            sum += nums[j]

        return sum
        