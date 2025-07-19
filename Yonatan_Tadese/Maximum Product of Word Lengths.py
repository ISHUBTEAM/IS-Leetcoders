from typing import Counter


def product():
    words = ["abcw","baz","foo","bar","xtfn","abcdef"] #16
    ans = 0
    
    wordSet = [set(words[i]) for i in range(len(words))]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(wordSet[i] & wordSet[j]) == 0:
                ans = max(ans, len(words[i]) * len(words[j])) 
    return ans


print(product())