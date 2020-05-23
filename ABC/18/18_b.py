S = input()
N = int(input())
n = len(S)
for i in range(N):
    l,r = map(int, input().split())
    temp = S[l-1:r]
    S = S[:l-1]+temp[::-1]+S[r:n]
print(S)