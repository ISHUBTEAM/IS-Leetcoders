def arraySum():
    nums = [1,4,3,2] #4
    # nums = [6,2,6,5,1,2] #9

    for i in nums:
        for j in range(len(nums)):
            print(min(i, j) + min(i, j))

 

print(arraySum())