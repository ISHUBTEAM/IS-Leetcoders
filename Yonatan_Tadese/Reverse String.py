def reverse():
    s = ["h","e","l","l","o"] # ["o","l","l","e","h"]
    s[:] = [s[-i -1] for i in range(len(s))]
    return s

print(reverse())