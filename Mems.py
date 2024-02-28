schet = 0
a = int(input())

dlin = len(str(a))

for _ in range(int(dlin)):
    b = a % 10
    a = a // 10
    if b % 2 == 0:
        schet = schet + 1

print(schet)
