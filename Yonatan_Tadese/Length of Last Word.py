class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        txtArr = s.split()
        txt = txtArr[len(txtArr) - 1]
        return len(txt)