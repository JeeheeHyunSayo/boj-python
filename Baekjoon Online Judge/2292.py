import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    cnt =  1
    start = 2
    for i in range(1, n):
        sum = start + 6 * i
        cnt += 1
        start = sum
        if n < sum:
            break

    print(cnt)
