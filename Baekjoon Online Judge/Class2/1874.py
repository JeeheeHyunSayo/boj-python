import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
     arr.append(int(input()))

stack = []
next_push = 1 # 다음 target 에서도 next_push 가 쓰여야함
result = []
flag = True

for target in arr:
    while next_push <= target:
        stack.append(next_push)
        result.append('+')
        next_push += 1
    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        flag = False
        break

if not flag:
    print("NO")
else:
    print('\n'.join(map(str, result)))