def transpose():
    matrix = [[1,2,3],[4,5,6]]
    res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return res

print(transpose())