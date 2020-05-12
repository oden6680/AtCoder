N,M,X = map(int, input().split())
C = []
A = []
for i in range(N):
    a = list(map(int, input().split()))
    C.append(a[0])
    A.append(a[1:M+1])
for i in range(2**N:)