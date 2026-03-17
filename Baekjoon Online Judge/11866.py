import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())
q = deque(range(1, n+1))
result = []

# popleft 는 큐의 길이를 훼손
# '회전'의 개념

while q:
    for _ in range(m-1): # 1, 2번째까지
        q.append(q.popleft()) # 1 지우고 뒤에, 2 지우고 뒤에
    result.append(q.popleft()) # 3번째 원소 result 에 append

print("<" + ", ".join(map(str, result)) + ">") # 문자열 출력 


