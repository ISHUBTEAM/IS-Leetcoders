class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
    
        if target not in nums:
            nums.append(target)
            nums.sort()
        
        while start <= end:
            mid = int((start + end) / 2)
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return 0
        

''' loop trying lol'''
# print(len(test))

# new_num = []

# for i in range(1, len(nums) + target):
#     new_num.append(i)
   
# if target not in nums:
#     if target > len(nums):
#         for k in range(len(nums), len(nums) + target):
#             if k == target:
#                 print(k)
#     else:  
#         for j in range(len(new_num)):
#             if new_num[j] == target:
#                 print(j)
    


# max = nums[0]
# for i in range(len(nums)):
#     if nums[i] == target:
#         print(i)        
#     elif target > nums[i]:
#         max = i
#         print(nums[i])
    
# if max >= len(nums) - 1:
#     nums.insert(max + 1, target)
#     for i in range(len(nums)):
#         if nums[i] == target:
#             print(i)
        