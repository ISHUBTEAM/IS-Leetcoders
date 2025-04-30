def generate():
    n = 3 # ["((()))","(()())","(())()","()(())","()()()"]
    # n = 2 # ["(())","()()"]

    def parentheses(res, s, open, close):
        if open == 0 and close == 0:
            res.append(s)
        
        if open > 0:
            parentheses(res, s+"(", open-1, close)

        if close > 0 and open < close:
            parentheses(res, s+")", open, close-1)

    res = []
    parentheses(res, '', n, n)
    return res

print(generate())