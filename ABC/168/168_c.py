import math
A,B,H,M = map(int, input().split())
s1 = H*30+float(M/60)*30
s2 = M*6
sita = min(max(s1,s2)-min(s1,s2),(360-max(s1,s2))+min(s1,s2))
co = math.cos(math.radians(sita))
res = (B**2)+(A**2)+(-2*B*A*co)
print(math.sqrt(res))