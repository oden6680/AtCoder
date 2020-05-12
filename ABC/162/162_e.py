n,k = map(int, input().split())
cnt = 0
for i in range(k+1):
    cnt += (i+1)*((k//(i+1))**(k-i))
print (cnt%(10**9+7))