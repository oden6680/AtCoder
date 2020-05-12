import collections
N = int(input())
A = list(map(int, input().split()))
L = collections.Counter(A)
for i in range(N):
    print(L[i+1])