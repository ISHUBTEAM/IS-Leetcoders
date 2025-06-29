def morse():
    words = ["gin","zen","gig","msg"]
    codeArr = [".-", "-...", "-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

    res = []
    diff = 0

    for i  in words:
        code = ''
        for j in i:
            code += codeArr[ord(j) - 97]
        if code not in res:
            diff += 1
        res.append(code)


    return diff

print(morse())