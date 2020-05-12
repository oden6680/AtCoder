n = int(input())
w = list(map(int, input().split()))
center = sum(w)//2
sml = 0
i = 0
while sml < center:
    sml += w[i]
    i += 1
i -= 1
smr = sum(w)-sml
if sml-smr > smr+w[i]-(sml-w[i]):
    print(smr+w[i]-(sml-w[i]))
else:
    print(sml-smr)