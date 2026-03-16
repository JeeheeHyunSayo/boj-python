n = int(input())

for _ in range(n):
    s = input()
    stack = []
    flag = True

    for string in s:
        if '(' in string:
            stack.append(string)
        else: # ')', 문제조건 '(' 와 ')' 로만 이루어짐
            if not stack:
                flag = False
                continue
            stack.pop()
    if stack:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")