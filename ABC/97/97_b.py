X = int(input())
res = 1
for i in range(2,32):
    p = 2
    while i**p <= X:
        if res < i**p:
            res = i**p
        p += 1
print(res)