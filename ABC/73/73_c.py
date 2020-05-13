N = int(input())
A = set()
for i in range(N):
    n = int(input())
    if not (n in A):
        A.add(n)
    else:
        A.remove(n)
print(len(A))