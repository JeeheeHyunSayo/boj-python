import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 도감에 수록되어 있는 포켓몬 개수, 내가 맞춰야 하는 문제의 개수
pocketName = {}
pocketNum = {}

for i in range(n):
    name = input().rstrip()
    pocketName[name] = i+1
    pocketNum[i+1] = name

for _ in range(m):
    q = input().rstrip()
    if q.isdigit():
        q = int(q)
        print(pocketNum[q])

    else:
        print(pocketName[q])