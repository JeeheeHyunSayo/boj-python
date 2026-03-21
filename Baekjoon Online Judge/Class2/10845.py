import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n = int(input())
result = []

for _ in range(n):
    command = input().split()
    if len(command) == 2:
        s, n = command[0], command[1]
    else:
        s = command[0]

    if s == 'push':
        q.append(int(n))
    elif s == 'pop':
        if len(q) > 0:
            result.append(q.popleft())
        else:
            result.append(-1)
    elif s == 'size':
        result.append(len(q))
    elif s == 'empty':
        if len(q) == 0:
            result.append(1)
        else:
            result.append(0)
    elif s == 'front':
        if len(q) > 0:
            result.append(q[0])
        else:
            result.append(-1)
    elif s == 'back':
        if len(q) > 0:
            result.append(q[-1])
        else:
            result.append(-1)

print('\n'.join(map(str, result)))


