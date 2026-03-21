import sys
input = sys.stdin.readline

n = int(input())
stack = [] # First In Last Out, 마지막에 들어온 원소가 먼저 나감
result = []

for _ in range(n):
    command = input().split()
    if len(command) == 2:
        s, n = command[0], command[1]
    else:
        s = command[0]

    if s == 'push':
        stack.append(int(n))
    elif s == 'top':
        if len(stack) > 0:
            result.append(stack[-1])
        else:
            result.append(-1)
    elif s == 'size':
        result.append(len(stack))
    elif s == 'empty':
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif s == 'pop':
        if len(stack) > 0:
            result.append(stack.pop())
        else:
            result.append(-1)

print('\n'.join(map(str, result)))