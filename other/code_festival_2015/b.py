import collections
N,M = map(int, input().split())
A = list(map(int, input().split()))
c = collections.Counter(A)
most = c.most_common()[0][1]

if len(c) <= 1:
    mos2 = 0
else:
    mos2 = c.most_common()[1][1]

if most > N//2 and most != mos2:
    print(c.most_common()[0][0])
else:
    print("?")