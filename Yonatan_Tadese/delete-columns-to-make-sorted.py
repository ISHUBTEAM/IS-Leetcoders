def delCol():
    strs = ["zyx","wvu","tsr"]
    # z y   x
    # w v   u
    # t s   r

    remove_count = 0
    for col in zip(*strs):
        if list(col) != sorted(col):
            remove_count += 1
    return remove_count

print(delCol())