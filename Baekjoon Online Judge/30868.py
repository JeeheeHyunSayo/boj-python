t = int(input())  # 후보의 수
for _ in range(t):
    n = int(input()) # 각 후보가 받은 표의 수
    answer = ''
    if n >= 5:
        fiveCnt = n // 5
        answer += '++++ ' * fiveCnt
        leftover = n % 5
        answer += '|' * leftover
    else:
        answer += '|' * n
    print(answer)
