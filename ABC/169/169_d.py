N = int(input())
ar =  set()

def is_prime(q):
    if q == 1:
        return True
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1
if N == 1:
    print(0)
    exit()
while N > 0:
    if is_prime(N):
        ar.add(N)
        break
    for i in range(2,(N//2)+2):
        if N%i == 0 and (not i in ar):
            ar.add(i)
            break
    N = N//i
print(len(ar))