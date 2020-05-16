N = int(input())
A = tuple(map(int, input().split()))
res = [0]*N
for i in range(N):
    cnt = 1
    x = A[i]
    while x != i+1:
        x = A[x-1]
        cnt += 1
    res[i] = cnt
print(*res)