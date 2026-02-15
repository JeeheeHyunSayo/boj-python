# string.count() 를 10번 호출 : 비효율적
# 리스트가 필요 없다, 저장할 필요 없이 바로 곱해도 됨

import sys

if __name__ == '__main__':
    input = sys.stdin.readline

    num = 1
    for _ in range(3):
        num *= int(input()) # A * B * C wow~

    count = [0] * 10 # 0 ~ 9 개수 저장
    for ch in str(num):
        count[int(ch)] += 1  # 인덱스로 저장

    for c in count:
        print(c)
