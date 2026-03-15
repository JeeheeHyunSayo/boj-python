n = int(input())
dot = []
for _ in range(n):
    x, y = map(int, input().split())
    dot.append((x, y))

dot.sort(key=lambda x:(x[0], x[1]))
for x, y in dot:
    print(x, y)