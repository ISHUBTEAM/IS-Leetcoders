class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
       
        if len(s) != len(goal):
            return False

        letters = list(s)

        for _ in range(len(s)):
            
            first = letters.pop(0)
            letters.append(first)

            if ''.join(letters) == goal:
                return True

        return False
