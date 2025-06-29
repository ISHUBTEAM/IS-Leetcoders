def duplicate():
    arr = [1,0,2,3,0,4,5,0]
    n = len(arr)            
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            i += 1
        i += 1
    for j in range(len(arr)):
        if n <= j:
            arr.pop()
    return arr

print(duplicate())