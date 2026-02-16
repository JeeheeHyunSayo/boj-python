import sys
import math

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input()) # 참가자 수
    arr = list(map(int, input().split())) # 티셔츠 사이즈 별 신청자 수
    t, p = map(int, input().split()) # 티셔츠와 펜의 묶음 수

    # 티셔츠 최소 묶음
    total = 0
    for num in arr:
        total += (math.ceil(num / t)) # 중요 // 와 /

    print(total)

    # 펜;;;
    print(n // p,  n % p)
