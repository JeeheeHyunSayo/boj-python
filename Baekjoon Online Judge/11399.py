import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.sort()

result = []
add = 0
for i in p:
    add += i
    result.append(add)

print(sum(result))