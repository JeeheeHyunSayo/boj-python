import sys

dp = [(0, 0)] * 41  #  n <= 40

def fin(n):
    if dp[n] != (0, 0):
        return dp[n]

    if n == 0:
        dp[n] = (1, 0)
    elif n == 1:
        dp[n] = (0, 1)
    else:
        a = fin(n-1)
        b = fin(n-2)
        dp[n] = (a[0] + b[0], a[1] + b[1])
    return dp[n]

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())

    for _ in range(n):
        num = int(input())
        result = fin(num)
        print(result[0], result[1])
