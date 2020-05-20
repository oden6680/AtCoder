A = int(input())
res = 0
for i in range(A//2+1):
    x = i
    y = A-i
    if x*y > res:
        res = x*y
print(res)