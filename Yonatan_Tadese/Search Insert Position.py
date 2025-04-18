nums = [1,3,5,6]
# target = 5 # 2
# target = 7 # 4
# target = 2 # 1

test = [2, 6, 13, 21, 36, 47, 63, 81, 97]
x = 13

start = 0
end = len(test) - 1

while start <= end:
    mid = int((start + end) / 2)
        
    if x == test[mid]:
        print(mid)
        break
    elif  x < test[mid]:
        end = mid - 1
    else:
        start = mid + 1
        

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
        