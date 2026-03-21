import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    for num in arr:
        flag = True # 숫자마다 플래그가 갱신되어야함
        if num == 1: # 1은 소수가 아님
            flag = False
            continue
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                flag = False
                break # 약수 발견 시

        if flag:
            cnt += 1

    print(cnt)
