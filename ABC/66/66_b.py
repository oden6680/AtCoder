S = list(input())
s = S[0]
res = 0
for i in range(1,len(S)-1):
    s += S[i]
    n = len(s)
    middle = n//2
    if n%2 == 1:
        continue
    elif s[:middle] == s[middle:n]:
        res = n
print(res)