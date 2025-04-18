x = 121 #true
y = str(x)
for i in range(0, len(y)):
    for j in range(len(y), 0):
        if i == j:
            print(True)
        else: 
            print(False)