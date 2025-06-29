class Solution:
    def isValid(self, s: str) -> bool:
        parent = {")":"(","]":"[","}":"{"}
        res = []

        for i in s:
            if i in parent.values():
                res.append(i)
            elif i in parent.keys():
                if not res or parent[i] != res.pop():
                    return False
                else:
                    continue
        return not res
        