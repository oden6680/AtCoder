S = input()
N = len(S)
f = S[:int((N-1)/2)]
l = S[int((N+1)/2):]

if f==l:
  print("Yes")
else:
  print("No")