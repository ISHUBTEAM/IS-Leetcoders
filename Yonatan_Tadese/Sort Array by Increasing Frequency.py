class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        
        theDict = dict()
        for i in nums:
            if i in theDict:
                theDict[i] = theDict[i] + 1
            else:
                theDict[i] = 1
        
        res = dict(sorted(theDict.items(), key=lambda x:x[1]))
        new = []
        for j in res:
            new.extend([j] * res[j])

        return new
        