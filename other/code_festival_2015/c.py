N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if M > N:
    print("NO")
    exit()
A.sort()
B.sort()
for i in range(M):
    if A[N-i-1] < B[M-i-1]:
        print("NO")
        exit()
print("YES")