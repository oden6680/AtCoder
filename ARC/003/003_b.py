N  = int(input())
A = []
for i in range(N):
    a = str(input())
    A.append(a[::-1])
A = sorted(A)
for i in range(N):
    print(A[i][::-1])