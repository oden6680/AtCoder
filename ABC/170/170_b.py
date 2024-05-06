X,Y = map(int, input().split())
for i in range(X+1):
    if 2*i + (X-i)*4 == Y:
        print("Yes")
        exit()
print("No")