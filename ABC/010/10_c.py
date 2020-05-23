import math
txa,tya,txb,tyb,T,V = map(int, input().split()) 
n = int(input())
max_move = T*V
for i in range(n):
    x,y = map(int, input().split())
    start_to_girl = math.sqrt((x-txa)**2+(y-tya)**2)
    girl_to_goal = math.sqrt((x-txb)**2+(y-tyb)**2)
    if start_to_girl + girl_to_goal <= max_move:
        print("YES")
        exit()
print("NO")