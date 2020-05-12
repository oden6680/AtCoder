N,M,Q = map(int, input().split())
a = []
b = []
c = []
d = []
for i in range(Q):
    A,B,C,D = map(int, input().split())
    a.append(A)
    b.append(B)
    c.append(C)
    d.append(D)
num = [1]*N
for i in range(Q):
    