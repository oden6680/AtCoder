a = list(input())
b = list(input())
c = list(input())
now_person = a
a_i = 0
b_i = -1
c_i = -1
now_person_i = 0
while True:
    if now_person_i == len(now_person):
      break
    if now_person[now_person_i] == 'a':
        now_person = a
        a_i += 1
        now_person_i = a_i
    elif now_person[now_person_i] == 'b':
        now_person = b
        b_i += 1
        now_person_i = b_i
    elif now_person[now_person_i] == 'c':
        now_person = c
        c_i += 1
        now_person_i = c_i
if now_person == a:
    print("A")
elif now_person == b:
    print("B")
else:
    print("C")