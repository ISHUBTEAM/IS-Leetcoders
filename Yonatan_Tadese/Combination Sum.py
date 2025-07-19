def combination():
    candidates = [2,3,5]
    target = 8 #[[2,2,2,2],[2,3,3],[3,5]]

    result = []
    solution = []

    def backtrack(i, sum):
        if sum == target:
            result.append(solution[:])
            return
        if sum > target or i == len(candidates):
            return
        
        backtrack(i + 1, sum)

        solution.append(candidates[i])
        backtrack(i, sum + candidates[i])
        solution.pop()
    
    backtrack(0, 0)


# my try before I learn

    # for i in range(len(candidates)):
    #     if candidates[i] == target:
    #         res.append([candidates[i]])
    #     if candidates[i] > target:
    #         return        
    #     print('\n')
    #     for j in range(i + 1, len(candidates)):
    #         if candidates[i] + candidates[j] == target:
    #             res.append([candidates[i], candidates[j]])
            
    #         if candidates[i] + candidates[j] < target:
    #             for k in range(len(candidates)):
    #                 if candidates[i] * k + candidates[j] == target:
    #                     res.append([candidates[i] * k, candidates[j]])
                    
    # print(candidates[j])

    return result

print(combination())