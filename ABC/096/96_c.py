H,W = map(int,input().split())
S = []
for i in range(H):
    S.append(input())
for i in range(1,H-1):
    for j in range(1,W-1):
        if S[i][j]== "#" and S[i+1][j] == S[i][j+1] == S[i-1][j] == S[i][j-1] == ".":
            print("No")
            exit()
print("Yes")
