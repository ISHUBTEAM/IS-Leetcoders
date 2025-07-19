def fairCandy():
    aliceSizes = [1,2]
    bobSizes = [2,3]

    diff = ((sum(aliceSizes) - sum(bobSizes)) // 2)

    for i in aliceSizes:
        b = i - diff
        if b in bobSizes:
            return [i, b]

print(fairCandy())