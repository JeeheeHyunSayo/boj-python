
import bisect
n = int(input())
arr1 = sorted(list(map(int, input().split())))

m = int(input())
arr2 = list(map(int, input().split())) # 출력 순서 유지

for x in arr2:
    i = bisect.bisect_left(arr1, x)

    if i < n and arr1[i] == x:
        print(1)
    else:
        print(0)