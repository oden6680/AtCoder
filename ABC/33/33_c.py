S = list(map(str, input().split('+')))
cnt = len(S)
for i in range(len(S)):
    if '0' in S[i]:
        cnt -= 1
print(cnt)