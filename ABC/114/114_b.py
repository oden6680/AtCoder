S = list(input())
dif_min = 10**9
for i in range(len(S)-2):
    if dif_min > abs(int(S[i]+S[i+1]+S[i+2])-753):
        dif_min = abs(int(S[i]+S[i+1]+S[i+2])-753)
print(dif_min)