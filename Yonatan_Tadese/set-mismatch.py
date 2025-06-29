def mismatch():
    nums = [2, 2]
    n = len(nums)
    fr = dict()
    duplicate = None
    missed = None
    for i in range(1, n + 1):
        if i not in nums:
            missed = i    
    for j in nums:
        if j in fr:
            duplicate = j
        else:
            fr[j] = 1    
    return [duplicate, missed]

print(mismatch())

'''
for i in range(0, n):
        for j in range(i + 1, n):
            print(i)
            print(j)
            print(nums[i])
            print(nums[j])
            if nums[i] == nums[j] % n:
                res.append(nums[i])
                res.append(nums[j] + 1)


'''