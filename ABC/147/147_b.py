s = list(input())
l = len(s)//2
cnt = 0
for i in range(l):
    j = len(s) - i - 1
    if s[i] != s[j]:
        cnt += 1
print(cnt)    