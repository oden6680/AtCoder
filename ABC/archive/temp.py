import collections #各要素の個数を数える
'''sample (出現回数順に抽出)
collections.Counter()
c = []
c.most_common() #出現回数順にソート
'''

import fractions #最小公倍数　最大公約数gcd(a,b)
'''sample (最小公倍数)
ans = a[0]
for i in range(1, N):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
print(ans)
'''

# N行の入力を配列として受け取る
'''
ca = [list(map(int, input().split())) for _ in range(N)]
'''

#bit全探索
'''
for i in range(2**N):
    for j in range(N):
        if (i >> j) & 1: #iを二進数で表したものを右にjだけシフトし、それが1かどうかの判定
            処理
'''

#素因数分解(素数別に二次元配列で返す)
'''
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
'''

#素数判定 (素数の時True)
'''
def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1
'''