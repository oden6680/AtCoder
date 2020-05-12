x,y,w = map(str,input().split())
x,y = int(x),int(y)
T = []
for i in range(9):
  T.append(input())
s = [None]*4
s[0]=[x,y]
if w == "R":
  for i in range(3):
    s[i+1] = [s[i][0]+1,s[i][1]]
elif w == "L":
  for i in range(3):
    s[i+1] = [s[i][0]-1,s[i][1]]
elif w == "U":
  for i in range(3):
    s[i+1] = [s[i][0],s[i][1]-1]
elif w == "D":
  for i in range(3):
    s[i+1] = [s[i][0],s[i][1]+1]
elif w == "RU":
  for i in range(3):
    s[i+1] = [s[i][0]+1,s[i][1]-1]
elif w == "RD":
  for i in range(3):
    s[i+1] = [s[i][0]+1,s[i][1]+1]
elif w == "LU":
  for i in range(3):
    s[i+1] = [s[i][0]-1,s[i][1]-1]
elif w == "LD":
  for i in range(3):
    s[i+1] = [s[i][0]-1,s[i][1]+1]
for i in range(1,4):
  x,y = s[i]
  if x <= 0:
    x = 2-x
  elif x >= 10:
    x = 18-x
  if y <= 0:
    y = 2-y
  elif y >= 10:
    y = 18-y
  s[i]=[x,y]
res = ""
for i in range(4):
  x,y = s[i]
  res += T[y-1][x-1]
print(res)