k = int(input())
stack = []
flag = True

for _ in range(k):
    n = int(input())
    if n != 0:
        stack.append(n)
    else:
        if not stack:
            flag = False
            continue
        stack.pop()

if flag:
    print(sum(stack))
else:
    print(0)