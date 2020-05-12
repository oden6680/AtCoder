import collections #各要素の個数を顔彫る時
'''sample (出現回数順に抽出)
collections.Counter()
c = []
c.most_common()
'''
import fractions #最小公倍数　最大公約数gcd(a,b)
'''sample (最大公約数)
ans = a[0]
for i in range(1, N):
    ans = ans * a[i] // fractions.gcd(ans, a[i])
print(ans)
'''