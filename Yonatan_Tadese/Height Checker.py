def check():
    heights = [1,1,4,2,1,3] #3
    sortHeight = sorted(heights)
    score = 0

    for i in range(len(heights)):
        if heights[i] != sortHeight[i]:
            score += 1



    return score

print(check())