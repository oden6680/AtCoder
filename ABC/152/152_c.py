N = int(input())
P = list(map(int, input().split()))
cnt = 0
min_n = P[0]
for i in range(N):
    if min_n >= P[i]:
        cnt += 1
        min_n = P[i]
print(cnt)