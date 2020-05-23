N = int(input())
a = list(map(int,input().split()))
res = 0
for i in a:
    while i%3==2 or i%2==0:
        i -= 1
        res +=1
print(res)