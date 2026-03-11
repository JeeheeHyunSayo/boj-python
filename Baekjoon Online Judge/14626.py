import sys
input = sys.stdin.readline

code = input().rstrip()
total = 0
v = 1
for i in range(len(code)):
    if code[i] == '*':
        if i % 2 == 1:
            v = 3
        continue
    if i % 2 == 0:
        total += int(code[i]) % 10
    else:
        total += int(code[i]) * 3 % 10


# 10으로 나눈 나머지 : 0 ~ 9
for x in range(10):
    if (x * v + total) % 10 == 0:
        print(x)
        break