class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result  = ""

        shortest = strs[0]
        for i in strs:
            if len(i) < len(shortest):
                shortest = i
            
        for j in range(len(shortest)):
            for k in strs:
                if k[j] != strs[0][j]:
                    return result
            result += strs[0][j]
        return result
        