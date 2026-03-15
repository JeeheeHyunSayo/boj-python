while True:
    s = input() # 매 문장 입력 받음
    flag = True # 문장마다 flag 변수 초기화
    stack = [] # 문장마다 stack (괄호를 넣을)  초기화

    if s == '.': # break 조건
        break

    for string in s:
        # '( '
        if string == '(':
            stack.append(string)
        # '['
        if string == '[':
            stack.append(string)
        # ')'
        if string == ')':
            if len(stack) == 0 or  stack[-1] != '(':
                flag = False
                break
            stack.pop()

        # ']'
        if string == ']':
            if len(stack) == 0  or stack[-1] != '[':
                flag = False
                break
            stack.pop()

    if stack:
        flag = False

    if not flag:
        print("no")
    else:
        print("yes")


