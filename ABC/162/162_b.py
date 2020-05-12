n = int(input())
cnt = 0
for i in range(n):
    if (i+1)%3 != 0 and (i+1)%5 !=0:
        cnt += i+1
print(cnt)