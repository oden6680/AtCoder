n = int(input())
s = list(input())
r = s.count('R')
g = s.count('G')
b = s.count('B')
cnt = r*g*b
for i in range((len(s)-1)//2):
    for j in range(i+1,len(s)-i-1):
        if s[j-(i+1)] != s[j] and s[j] != s[j+(i+1)] and s[j-(i+1)] != s[j+(i+1)]:
            cnt-=1
print(cnt)