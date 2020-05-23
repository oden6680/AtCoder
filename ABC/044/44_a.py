N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if K > N:
    print(N*X)
else:
    print(K*X + (N-K)*Y)