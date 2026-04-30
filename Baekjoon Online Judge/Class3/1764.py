import sys
input = sys.stdin.readline

n, m = map(int, input().split())
noListen = {}
noSee = {}

for i in range(n):
    name = input().rstrip()
    noListen[name] = i + 1

cnt = 0
result = []
for i in range(m):
    name = input().rstrip()
    if name in noListen:
        cnt += 1
        result.append(name)

result.sort() # 알파벳 순 나열 조건

print(cnt)
print('\n'.join(result))