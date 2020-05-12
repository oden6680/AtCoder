X = int(input())
if X == 2:
    print(2)
    exit()
while True:
    N = int(X**0.5)
    for i in range(1,N):
        if X % (i+1) == 0:
            break
        else:
          if i == N - 1:
            print(X)
            exit()
    X += 1