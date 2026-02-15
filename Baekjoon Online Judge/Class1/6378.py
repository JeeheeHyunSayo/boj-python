while True:
    n = input()
    if n == '0': break
    while True:
        answer = 0 # 이거 때문에 ...
        for number in n:
            answer += int(number)
        total = answer
        if total < 10:
            print(total)
            break
        n = str(total)





