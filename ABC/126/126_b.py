s = list(input())
l = int(s[0]+s[1])
r = int(s[2]+s[3])
if 1 <= l <= 12 and 1 <= r <= 12:
    print("AMBIGUOUS")
elif 1 <= l <= 12:
    print("MMYY")
elif 1 <= r <= 12:
    print("YYMM")
else:
    print("NA")