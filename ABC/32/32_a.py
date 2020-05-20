import fractions
a = int(input())
b = int(input())
n = int(input())
lcm = a*b//fractions.gcd(a,b)
while n%lcm != 0:
    n += 1
print(n)