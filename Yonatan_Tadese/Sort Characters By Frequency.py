from typing import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sort_chars = sorted(count, key=count.get, reverse=True)

        res = ''
        for i in sort_chars:
            res += i * count[i]    
        return res
        

# My first attempt

# res = ''
    # for i in range(len(s) - 1, -1, -1):
    #     res += (s[i])
    # a = ''.join(sorted(res))