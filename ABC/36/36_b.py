N = int(input())
s = []
for i in range(N):
    S = input()
    s.append(S)
for i in range(N):
    temp = ""
    for j in range(N):
        temp += s[j][i]
    print(temp[::-1])