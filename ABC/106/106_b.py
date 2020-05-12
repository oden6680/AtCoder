N = int(input())
res = 0
for i in range(1,N+1):
    div_cnt = 0
    for j in range(1,i+1):
        if i%j == 0:
            div_cnt += 1
    if div_cnt == 8 and i%2 == 1:
        res += 1
print(res)