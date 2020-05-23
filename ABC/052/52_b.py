N = int(input())
s = list(input())
res = []
cnt = 0
for i in range(N):
    if s[i] == 'I':
        cnt += 1
    elif s[i] == 'D':
        cnt -= 1
    res.append(cnt)
print(max(max(res),0))