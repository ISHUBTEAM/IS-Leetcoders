def ranking():
    score = [10,3,8,9,4]
    #["Gold Medal","5","Bronze Medal","Silver Medal","4"]

    sortScore = sorted(score,reverse=True)

    rank = dict()

    for i in range(0, len(sortScore)):
        if i == 0:
            ind = score.index(sortScore[i])            
            rank[ind] = 'Gold Medal'
        elif i == 1:
            ind = score.index(sortScore[i])
            rank[ind] = 'Silver Medal'
        elif i == 2:
            ind = score.index(sortScore[i])
            rank[ind] = 'Bronze Medal'
        # else:
        #     rank[i] = i
        


    return rank

print(ranking())