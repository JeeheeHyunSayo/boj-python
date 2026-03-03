# cnt = 1
# start = a - b
#
#
# while True: # 하루 하루 시뮬레이션 해서 v 가 너무 크면 반복 횟수가 너무 많아서 시간 포과
#     start += a
#     if start > v:
#         cnt += 1
#         print(cnt)
#         break
#     else:
#         start -= b
#     cnt += 1
#


# 마지막 날에는 미끌어지지 않음 (v - a)
# 실제로 하루에 증가하는 높이 ( a - b)
import math
a, b, v = tuple(map(int, input().split()))
print(math.ceil((v - a) / (a - b)) + 1)
