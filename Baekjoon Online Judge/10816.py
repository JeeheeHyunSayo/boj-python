from collections import Counter # 원소의 개수를 셈

n = int(input())
arr1 = input().split()

m = int(input())
arr2 = input().split()

count = Counter(arr1)
for i in arr2:
    print(count[i], end=' ')

# count = {}
# list.count() 의 시간 복잡도는 짱짱 큼
# for i in arr1:
#     count[i] = count.get(i, 0) + 1
#
# for i in arr2:
#     print(count.get(i, 0), end=' ')
