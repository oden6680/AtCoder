N = int(input())
S = []
P = []
for i in range(N):
    s,p = map(str, input().split())
    S.append(s)
    P.append(int(p))
SUM = sum(P)
for i in range(N):
    if P[i] > SUM//2:
        print(S[i])
        exit()
print("atcoder")