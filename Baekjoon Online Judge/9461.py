import sys
input = sys.stdin.readline

t = int(input())
max_k = 100 # 1 <= n <= K

dp = [0] * (max_k+1)
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
# 점화식 적용
for i in range(6, max_k+1):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(t):
    n = int(input())
    print(dp[n])