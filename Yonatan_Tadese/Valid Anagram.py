def anagram():
    s = "a" 
    t = "ab" #false

    if len(s) != len(t):
        return False

    arr_s = dict()
    for i in s:
        if i not in t:
            return False
        if i in arr_s:
            arr_s[i] = arr_s[i] + 1
        else:
            arr_s[i] = 1

    arr_t = dict()
    for j in t:
        if j in arr_t:
            arr_t[j] = arr_t[j] + 1
        else:
            arr_t[j] = 1

    for k in arr_s:
        if arr_s[k] != arr_t[k]:
            return False
    return True

print(anagram())