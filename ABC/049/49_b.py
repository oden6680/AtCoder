H,W = map(int, input().split())
C = []
for i in range(H):
    c = input()
    C.append(c)
    C.append(c)
for i in range(2*H):
    print(C[i])