# 입력 자료형 : 3백만
import sys
input = sys.stdin.readline
s = set()
n = int(input()) #

for _ in range(n):
    command = input().split()
    if len(command) > 1:
        c,i = command[0], int(command[1]) #
    else:
        c,i = command[0], 0

    if c == 'add':
        s.add(i)
    elif c == 'remove':
        s.discard(i)
    elif c == 'check':
        print(1 if i in s else 0)
    elif c == 'toggle':
        if i in s:
            s.discard(i)
        else:
            s.add(i)
    elif c == 'all':
        s = set(range(1, 21)) #
    elif c == 'empty':
        s = set()

