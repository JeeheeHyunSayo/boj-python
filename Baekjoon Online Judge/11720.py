import sys
input = sys.stdin.readline

n = int(input())
m = input().rstrip()

total = 0
for i in range(n):
    total += int(m[i])

print(total)