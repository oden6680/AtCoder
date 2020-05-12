N = int(input())
pre_t = 0
pre_x = 0
pre_y = 0
for i in range(N):
    t,x,y = map(int, input().split())
    if (t%2)+(x+y)%2 == 1 or x+y > t or abs(pre_x-x)+abs(pre_y-y) > (t-pre_t):
        print("No")
        exit()
    pre_t = t
    pre_x = x
    pre_y = y
print("Yes")