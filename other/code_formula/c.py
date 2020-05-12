S = list(input().split())
res = []
for i in S:
    if '@' in i:
        res.append(i[(i.rfind('@'):-1)])
S = set(S)
S = list(S)
S = sorted(S)
for i in S:
    print(i)