N = int(input())
N = N/1000
if N < 0.1:
  vv = 0
elif 0.1 <= N <= 5:
  vv = 10 * N
elif 6 <= N <= 30:
  vv = N + 50
elif 35 <= N <= 70:
  vv = (N-30)/5 + 80
elif N > 70:
  vv = 89
print(str(int(vv)).zfill(2))