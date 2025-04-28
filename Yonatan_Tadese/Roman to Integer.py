class Solution:
    def romanToInt(self, s: str) -> int:
        source = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        
        total = 0    
        for i in range(len(s)):
            if i <= len(s) - 2 and source[s[i]] < source[s[(i + 1)]]:
                minimize = source[s[(i + 1)]] - source[s[i]]
                total += minimize
                total -= source[s[(i + 1)]]
                total -= source[s[i]]
            total += source[s[i]]
        return total
        