S = input()
K = int(input())
pas = set()
for i in range(len(S)-K+1):
    pas.add(S[i:i+K+1])
print(len(pas))