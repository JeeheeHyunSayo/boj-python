import sys
input = sys.stdin.readline

n = int(input())
arr = {input().rstrip() for _ in range(n)}
print('\n'.join(sorted(arr, key=lambda x: (len(x), x))))
