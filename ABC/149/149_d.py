N,K = map(int, input().split())
R,S,P = map(int, input().split())
T = list(input())
win_point = {"r":P,"p":S,"s":R}
score = 0
for i in range(K):
    score += win_point[T[i]]
for i in range(K,N):
    if T[i] == T[i-K]:
        T[i] = "."
        continue
    score += win_point[T[i]]
print(score)