class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dictionary = dict()
        for i in range(0, len(heights)):
            dictionary[heights[i]] = names[i]

        test = dict(sorted(dictionary.items(), reverse=True))
        res = list(test.values())
        return res
        