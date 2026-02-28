import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    arr = list(map(int, input().split()))
    m = max(arr)
    total = sum((i / m ) * 100 for i in arr)
    print(total/len(arr))

