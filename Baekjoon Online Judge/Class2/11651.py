n = int(input())
dot = []
for _ in range(n):
    x, y = map(int, input().split())
    dot.append((x,y))

dot.sort(key=lambda x:(x[1],x[0]))
for x, y in dot:
    print(x, y)