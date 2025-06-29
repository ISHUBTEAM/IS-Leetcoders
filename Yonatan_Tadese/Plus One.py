class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a = ''
        ans = []
        for i in digits:
            a += str(i)
        b = int(a) + 1

        for j in str(b):
            ans.append(int(j))
            
        return ans

        