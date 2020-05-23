N,M,Q = map(int, input().split())
u = []
v = []
for i in range(M):
    U,V = map(int, input().split())
    u.append(U)
    v.append(V)
c = list(map(int, input().split()))
for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        