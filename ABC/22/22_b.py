N = int(input())
A = set()
res = 0
for i in range(N):
    a = int(input())
    if a in A:
        res += 1
    else:
        A.add(a)
print(res)