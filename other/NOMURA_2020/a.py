H1,M1,H2,M2,K = map(int, input().split())
H1_t = H1*60+M1
H2_t = H2*60+M2
time = max(H1_t,H2_t) - min(H1_t,H2_t)
if time > K:
    print(time - K)
else:
    print(0)