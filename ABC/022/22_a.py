N,S,T = map(int, input().split())
W = int(input())
res = 0
if S <= W <= T:
    res += 1
for i in range(N-1):
    a = int(input())
    W += a
    if S <= W <= T:
        res += 1
print(res)