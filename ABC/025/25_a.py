S = list(input())
N = int(input())
res = []
for i in range(5):
    for j in range(5):
        res.append(S[i]+S[j])
res.sort()
print(res[N-1])