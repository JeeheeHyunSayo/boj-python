import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    mValue = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                total = arr[i] + arr[j] + arr[k]
                if total <= m:
                    mValue = max(mValue, total)
    print(mValue)