import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))
arr2 = [elem  for elem in arr if elem < x ]

print(' '.join(map(str, arr2)))
