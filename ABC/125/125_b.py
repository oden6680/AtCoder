N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
res = 0
for i in range(N):
    if V[i] > C[i]:
        res += V[i]-C[i]
print(res)