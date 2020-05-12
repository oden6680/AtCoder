A = int(input())
for i in range(10,10001):
    m = 1
    tmp = 0
    for j in str(i)[::-1]:
        tmp += m * int(j)
        m *= i
    if tmp == A:
        print(i)
        break
else:
    print(-1)
