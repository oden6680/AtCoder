C = []
for i in range(3):
    C.append(list(map(int, input().split())))
for i in range(1,101):
    b1 = C[0][0]-i
    b2 = C[0][1]-i
    b3 = C[0][2]-i
    a2 = C[1][0]-b1
    a3 = C[2][0]-b1
    if [[i+b1,i+b2,i+b3],[a2+b1,a2+b2,a2+b3],[a3+b1,a3+b2,a3+b3]] == C:
        print("Yes")
        exit()
print("No")