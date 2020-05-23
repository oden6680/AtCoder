s = list(input())
res = []
for i in range(len(s)):
    if s[i] != 'B':
        res.append(s[i])
    elif len(res) != 0:
        del res[-1]
print(''.join(res))