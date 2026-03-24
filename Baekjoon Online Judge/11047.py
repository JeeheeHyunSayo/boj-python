import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = {}
for _ in range(n):
    v = int(input())
    money[v] = 0

money_sorted = dict(sorted(money.items(), key=lambda x:x[0], reverse=True))
for v in money_sorted.keys():
    if v > k:
        continue
    else:
        cnt = k // v
        k -= cnt * v
        money_sorted[v] = cnt

print(sum(money_sorted.values()))
