H,W = map(int, input().split())
grid = []
grid.append(["."]*(W+2))
for i in range(H):
    s = ["."]+list(input())+["."]
    grid.append(s)
grid.append(["."]*(W+2))
for i in range(1,H+1):
    for j in range(1,W+1):
        if grid[i][j] != "#":
            temp = [grid[i-1][j-1],grid[i-1][j],grid[i-1][j+1],grid[i][j-1],grid[i][j+1],grid[i+1][j-1],grid[i+1][j],grid[i+1][j+1]]
            bom = str(temp.count("#"))
            grid[i][j] = bom
for i in range(1,H+1):
    print("".join(grid[i][1:W+1]))