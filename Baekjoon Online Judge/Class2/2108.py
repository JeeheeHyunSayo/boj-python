import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

arr = sorted(arr)

# 산술 평균, 첫째자리에서 반올림
print(round(sum(arr)/len(arr)))

# 중앙값
print(arr[len(arr)//2])

# 최빈값, 두 번째로 작은 값
counter = Counter(arr)

# counter 는 sort() 가 없음 -> 최빈값만 걸러서
max_cnt = max(counter.values())
max_arr = [k for k, v in counter.items() if v == max_cnt]
max_arr.sort()

if len(max_arr) >= 2:
    print(max_arr[1])
else:
    print(max_arr[0])
# 범위 : max() - min()
print(max(arr) - min(arr))