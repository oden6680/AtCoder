N = int(input())
S = []
for i in range(N):
  S.append(list(input()))

for i in range(N-2,-1,-1):
  for j in range(2*N-1):
    if S[i][j] == '#':
      flag = False
      for k in range(3):
        if S[i+1][j-1+k] == 'X':
          flag = True
      if flag:
        S[i][j] = 'X'

for i in S:
  print(''.join(i))