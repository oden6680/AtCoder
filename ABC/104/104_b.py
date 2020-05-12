S = input()
flag = True
if S[0] != 'A':
  flag = False
elif S[2:-1].count('C') != 1:
  flag = False
else:
  for s in S[1:]:
    if s not in 'abcdefghijklmnopqrstuvwxyzC':
      flag = False
      break
if flag:
    print("AC")
else:
    print("WA")