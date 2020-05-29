import collections #各要素の個数を顔彫る時
'''sample (出現回数順に抽出)
collections.Counter()
c = []
c.most_common()
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