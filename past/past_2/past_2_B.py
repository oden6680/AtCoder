S = list(input())
a_cnt = S.count("a")
b_cnt = S.count("b")
c_cnt = S.count("c")
if a_cnt > b_cnt and a_cnt > c_cnt:
    print("a")
elif b_cnt > a_cnt and b_cnt > c_cnt:
    print("b")
else:
    print("c")