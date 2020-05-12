N = int(input())
S = []
for i in range(N):
    S.append(input())
T = []
M = int(input())
for i in range(M):
    T.append(input())
res = 0
for i in range(N):
    temp = S.count(S[i])-T.count(S[i])
    if res < temp:
        res = temp
print(res)