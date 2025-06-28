def diaDif():
    # 11,   2,  4
    # 4,    5,  6
    # 10,   8, -12
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    n = len(arr)
    
    left_dia = []
    right_dia = []

    for i in range(n):
        left_dia.append(arr[i][i])

    for i in range(n):
        j = n - i - 1
        right_dia.append(arr[i][j])

    return abs(sum(left_dia) - sum(right_dia))

print(diaDif())
