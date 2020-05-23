N,A,B = map(int, input().split())
cnt = 0
res = 0
for i in range(1,N+1):
    sums = 0
    x = i
    while x > 0:
        sums += x%10
        x = x//10
    if A <= sums <= B:
        res += i
print(res)