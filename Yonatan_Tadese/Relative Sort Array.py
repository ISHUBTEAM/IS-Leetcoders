def relative():
    arr1 = [2,3,1,3,2,4,6,7,9,2,19]
    arr2 = [2,1,4,3,9,6] #[2,2,2,1,4,3,3,9,6,7,19]

    arr2_dict = dict()
    for i in arr1:
        if i in arr2_dict:
            arr2_dict[i] = i + 1
        else:
            arr2_dict[i] = 1 

    res = [j for j in arr2]


    # for i in arr1:

    #     if i not in arr2:
    #         res.append(i)

    for i in arr1:
        if i in arr2_dict:
            # print(arr2_dict[i])
            if arr2_dict[i] > 1:
                res.append(i)
        else:
            res.append(i)
    
    return res

print(relative())