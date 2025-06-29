def miniMax():
    arr = [1, 2, 3, 4, 5]
    arr.sort()

    return [sum(arr[:len(arr) - 1]), sum(arr[1:])]

print(miniMax())