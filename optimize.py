str = [[] for i in range(25)]
forLoopParam = ""
rightHandParam = [[] for i in range(10)]
leftHandParam = ""
j = k = i = m = n = q = s = 0
flag = [0] * 10
count = [0] * 10

print("\nInput the loop to be optimized:\n")

str[0] = input()
while str[k][i] != ";":
    i += 1
while str[k][i] != ";":
    i += 1
while str[k][i] != ")":
    if str[k][i].isalpha():
        forLoopParam += str[k][i]
    i += 1
i = 0
str[0] = input()
while str[0][i] != "{":
    print(str[0])
    i += 1
k = 0
while True:
    str[k] = input()
    if str[k][0] == "}":
        break
    while str[k][i] != "=":
        i += 1
    leftHandParam += str[k][i - 2]
    k += 1
    i = 0
for m in range(k):
    while str[m][i] != "=":
        i += 1
    while str[m][i] != ";":
        if str[m][i].isalpha():
            rightHandParam[m].append(str[m][i])
            count[m] += 1
        i += 1
    i = 0
for m in range(k):
    for s in range(count[m]):
        for i in range(len(leftHandParam)):
            if rightHandParam[m][s] == leftHandParam[i]:
                flag[m] = 1

print("Optimized code:\n")
for i in range(k):
    for q in range(len(forLoopParam)):
        if leftHandParam[i] == forLoopParam[q]:
            flag[i] = 1
    for m in range(k):
        for s in range(count[m]):
            for j in range(len(forLoopParam)):
                if rightHandParam[m][s] == forLoopParam[j]:
                    flag[i] = 1

for i in range(k):
    if flag[i] == 1:
        print(str[i])
print(str[k])  # DISPLAYING THE END FLOWER BRACE }.
for i in range(k):
    if flag[i] == 0:
        print(str[i])
