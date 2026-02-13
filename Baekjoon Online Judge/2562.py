import sys
input = sys.stdin.readline

arr = []
for _ in range(9):
    num = int(input())
    arr.append(num)

maxNum = max(arr)
print(maxNum)
print(arr.index(maxNum) + 1)