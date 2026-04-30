import sys
input = sys.stdin.readline

t = int(input())
dp = [0] * 11
dp[1], dp[2], dp[3] = 1, 2, 4
num = []
for _ in range(t):
    num = int(input())
    if num > 3:
        for i in range(4, num+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[num])