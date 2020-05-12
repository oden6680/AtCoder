S = input()
S = list(S.split(' '))
res = []
for i in S:
    if i != '':
        res.append(i)
print(','.join(res))