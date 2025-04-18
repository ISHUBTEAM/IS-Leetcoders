nums = [1,3,5,6]
# target = 5 # 2
# target = 7 # 4
target = 2

max = nums[0]
for i in range(len(nums)):
    if nums[i] == target:
        print(i)        
    elif target > nums[i]:
        max = i
        print(nums[i])
    
if max >= len(nums) - 1:
    nums.insert(max + 1, target)
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)
        