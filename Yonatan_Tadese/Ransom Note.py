def ransom():
    ransomNote = "aa"
    magazine = "ab" #true

    ransom_dict = dict()
    for r in ransomNote:
        if r in ransom_dict:        
            ransom_dict[r] = ransom_dict[r] + 1
        else:
            ransom_dict[r] = 1

    magazine_dict = dict()
    for m in magazine:
        if m in magazine_dict:        
            magazine_dict[m] = magazine_dict[m] + 1
        else:
            magazine_dict[m] = 1

    for i in ransom_dict:
        if ransom_dict[i] != magazine_dict[i]:
            return False
    return True
print(ransom())