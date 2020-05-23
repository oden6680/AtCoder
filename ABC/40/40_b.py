import math
n = int(input())
i = 1
res = 10**9
while i <= math.sqrt(n):
    w = n//i 
    dif = abs(w-i)
    if (dif + n%(w*i)) < res:
        res = dif + n%(w*i)
    i += 1
print(res)