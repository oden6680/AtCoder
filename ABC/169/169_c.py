import math
from decimal import *
exp = Decimal(10**23)
A,B = map(str, input().split())
res = int(A)*Decimal(B)
print(math.floor(res))