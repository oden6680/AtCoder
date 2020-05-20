S = list(input())
T = input()
cnt_q = 0
x = 0
y = 0
if T == "1":
    for i in range(len(S)):
        if S[i] == "L":
            x -= 1
        elif S[i] == "R":
            x += 1 
        elif S[i] == "U":
            y += 1
        elif S[i] == "D":
            y -= 1
        else:
            cnt_q += 1
    print(abs(x)+abs(y)+cnt_q)
elif T == "2":
    for i in range(len(S)):
        if S[i] == "L":
            x -= 1
        elif S[i] == "R":
            x += 1 
        elif S[i] == "U":
            y += 1
        elif S[i] == "D":
            y -= 1
        else:
            cnt_q += 1
    if cnt_q > abs(x):
        cnt_q -= abs(x)
        x = 0
    if cnt_q > abs(y):
        cnt_q -= abs(y)
        y = 0
    if x == 0 and y == 0:
        if cnt_q%2 == 0:
            print(0)
            exit()
        else:
            print(1)
            exit()
    print(abs(abs(x)+abs(y)-cnt_q))