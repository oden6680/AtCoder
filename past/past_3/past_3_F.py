import collections
N = int(input())
S = []
l = collections.deque()
r = collections.deque()
for i in range(N):
    S.append(list(input()))
if N == 1:
    print(S[i][0])
    exit()
for i in range(N//2):
    S_ = list(set(S[i]) & set(S[N-i-1]))
    if len(S_) == 0:
        print(-1)
        exit()
    l.append(S_[0])
    r.appendleft(S_[0])
l = list(l)
r = list(r)
if N%2:
    middle = S[N//2][0]
else:
    middle = ""
l.append(middle)
print("".join(l+r))