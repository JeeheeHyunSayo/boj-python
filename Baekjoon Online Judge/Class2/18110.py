import sys
from collections import deque

input = sys.stdin.readline
q = deque()

def myRound(x):
    return int(x + 0.5)

n = int(input())
m = myRound(n*0.15)

for _ in range(n):
    q.append(int(input()))

q = deque(sorted(q))

for i in range(m):
    if len(q) > 0:
        q.popleft()
        q.pop()

if len(q) > 0:
    print(myRound(sum(q)/len(q)))
else:
    print(0)