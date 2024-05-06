N = int(input())
A = []
B = []
for i in range(N):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)

cnt = 0
for i in range(N-1,-1,-1):
    if (A[i]+cnt)%B[i] == 0:
        continue
    cnt += B[i] - ((A[i]+cnt)%B[i])
print(cnt)