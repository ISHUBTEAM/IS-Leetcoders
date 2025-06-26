def flipping():
    image = [[1,1,0],[1,0,1],[0,0,0]]

    reverse = []
    for i in image:
        rev = []
        for j in range(len(i) - 1, -1, -1):
            rev.append(i[j])
        reverse.append(rev)
        
    invert = []
    for i in reverse:
        inv = []
        for j in i:
            if j == 1:
                inv.append(0)
            else:
                inv.append(1)
        invert.append(inv)


    return invert

print(flipping())