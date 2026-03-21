# n = int(input())
# arr = []
# for _  in range(n):
#     num = int(input())
#     arr.append(num)
#
# arr = sorted(arr)
# for i in arr:
#     print(i)

# import sys
# input = sys.stdin.readline
# n = int(input())
# arr = [int(input()) for _ in range(n)] # 숫자를 1천만개를 리스트에 저장 (터짐)
# arr.sort()
# print('\n'.join(map(str, arr)))


# 입력 개수 n이 크면 데이터를 그대로 저장하면 안됨
# 계수 정렬
# 문제 조건 : 자연수, 10,000 보다 작거나 같은 수 (인덱스 접근을 위해 10,001 칸을 만드는 것 )

import sys
input = sys.stdin.readline

n = int(input())
count = [0] * 10001

for _ in range(n):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for _  in range(count[i]):
            print(i)