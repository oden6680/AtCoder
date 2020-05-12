N = int(input())
K = list(map(int, input().split()))
a = [K[0]]
for i in range(N-2):
    a.append(min(K[i],K[i+1]))
a.append(K[-1])
print(*a)