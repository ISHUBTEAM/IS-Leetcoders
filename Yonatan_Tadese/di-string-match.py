def diMatch():
    s = "III" #[0,4,1,3,2]
    n = len(s)

    num_list = [x for x in range(0, len(s) + 1)]
    res = []
    for i in s:
        if i == 'I':
            small = min(num_list)
            res.append(small)
            num_list.remove(small)
            
        else: 
            high = max(num_list)
            res.append(high)
            num_list.remove(high)

    for j in num_list:
        res.append(j)

    return res

print(diMatch())