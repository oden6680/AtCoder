A = int(input())
B = int(input())
C = int(input())
point = [A,B,C]
ans = ["A","B","C"]
for i in range(3):
    if max(point) == point[i]:
        print(1)
    elif min(point) == point[i]:
        print(3)
    else:
        print(2)