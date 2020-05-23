N = int(input())
s = []
res = ""
for i in range(5):
    s.append(input())
for i in range(N):
    if s[0][i*4+1:i*4+4] != "###": #1,4
        if s[1][i*4+3] == "#":
            res += "4"
        else:
            res += "1"
    elif s[1][i*4+1:i*4+4] == "#.#": #0,8,9
        if s[2][i*4+1:i*4+4] == "#.#":
            res += "0"
        else:
            if s[3][i*4+1] == "#":
                res += "8"
            else:
                res += "9"
    elif s[1][i*4+1:i*4+4] == "..#": #2,3,7
        if s[2][i*4+2] == ".":
            res += "7"
        else:
            if s[3][i*4+1] == "#":
                res += "2"
            else:
                res += "3"
    else:
        if s[3][i*4+1] == "#":
            res += "6"
        else:
            res += "5"
print(res)