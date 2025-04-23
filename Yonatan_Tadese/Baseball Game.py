class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for i in operations:
            if i == 'C':
                if len(score) >= 1:
                    score.pop(len(score) - 1)  
                else:
                    score.clear()    
            elif i == 'D':
                last = score[len(score) - 1]
                score.append(int(last) * 2)
            elif i == '+':
                last = score[len(score) - 1]
                beforeLast = score[len(score) - 2]
                score.append(int(last) + int(beforeLast))
            else:
                score.append(i)
        
        total = 0
        for k in score:
            total += int(k) 

        return total
        