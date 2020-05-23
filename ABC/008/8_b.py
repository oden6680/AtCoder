N = int(input())
res = dict()
for i in range(N):
    s = input()
    if s in res:
        res[s] += 1
    else:
        res[s] = 1
print(max(res,key = res.get))