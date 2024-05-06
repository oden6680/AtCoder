N = int(input())
A = list(map(int, input().split()))


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

cnt = 0
res = set()
for i in range(N):
    div = make_divisors(A[i])
    res = (set(div) | res)
print(N - len(res & set(A)))