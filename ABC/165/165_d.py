A,B,N = map(int, input().split())
if B == 1 or A == 1:
    print(0)
    exit()
if B > N or N == 1:
    res = int(A*N/B)-A*int(N/B)
else:
    N = N - N%B - 1
    res = int(A*N/B)-A*int(N/B)
print(res)