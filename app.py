from fetch import *
f = open ('logo.txt','r')
print(''.join([line for line in f]))
amount = int(input("Enter number of Questions:"))
topics = input("Enter topic:")
a = getinfo(amount,topics)
b = separateques(a)
q = []
for i in b:
    q.append(separateoptandsol(i))
flag1 = 0
for x in q:
    for y in x:
        if y == "" or y == " ":
            continue
        if "?" in y:
            print(y)
        if flag1 > 0 and flag1 < 5:
            print(y)
        if "Solution" in y:
            if "1" in y:
                solution = 1
            elif "2" in y:
                solution = 2
            elif "3" in y:
                solution = 3
            elif "4" in y:
                solution = 4
        flag1 += 1
    flag1 = 0
        
        
    
        