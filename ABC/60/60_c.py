N,T = map(int, input().split())
t = list(map(int, input().split()))
cnt = T
cnt = 0
for i in range(0,N-1):
    cnt += min(T,t[i+1]-t[i])
print(cnt+T)