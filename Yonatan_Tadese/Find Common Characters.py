from typing import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = []

        common_count = Counter(words[0])
        for word in words[1:]:
            common_count &= Counter(word)

        common = list(common_count.elements())
        return common


''' These are my try and errors '''

# first_count = Counter(words[0])

# for i in words:
#     this_count = Counter(i)
    
#     for j in this_count:
#         this_count[j] = min(first_count[j],  this_count[j])

# print(Counter(words[0]))

        # print(j)
# for i in words[0]:
#     for k in range(len(i)):
#         print(i[k])

# all_char = []
# for i in words:
#     all_char.extend([j for j in i])
# all_char = list(set(all_char))

# common = []
# for k in all_char:
#     flag = True
#     for l in words:
#         if k not in l:
#             flag = False
#         if flag : common.append(k)

# print(common)

# set = [set(x) for x in words]
# for i in set:
#     print(i)

# for k in words:
#     set = [set(k) for x in words]
#     print((set(k)))

# for i in words:
#     # print(i)
#     print('\n')
#     for j in range(len(i)):
#         if i[j] == i[j]:
#             print(i[j])
        
        
    
        