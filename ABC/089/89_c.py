N = int(input())
cnt = [0]*5
for i in range(N):
    S = input()
    if S[0] == "M":
        cnt[0] += 1
    elif S[0] == "A":
        cnt[1] += 1
    elif S[0] == "R":
        cnt[2] += 1
    elif S[0] == "C":
        cnt[3] += 1
    elif S[0] == "H":
        cnt[4] += 1
res = 0
for i in range(4):
    for j in range(i+1,5):
        for k in range(j+1,5):
            res += cnt[i]*cnt[j]*cnt[k]
print(res)