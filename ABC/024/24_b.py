N,T = map(int, input().split())
A = []
for i in range(N):
    a = int(input())
    A.append(a)
total = 0
for i in range(N-1):
    total += min(T,A[i+1]-A[i])
print(total+T)