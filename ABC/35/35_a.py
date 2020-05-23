import fractions
W,H = map(int, input().split())
div = fractions.gcd(W,H)
if W//div == 4:
    print("4:3")
else:
    print("16:9")