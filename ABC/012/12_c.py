N = int(input())
N = 2025 - N
for i in range(1,10):
    for j in range(1,10):
        if i*j == N:
            print(str(i)+" x "+str(j))