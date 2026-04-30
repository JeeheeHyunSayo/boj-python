n = int(input())
score = [0] # 1-index
for _ in range(n):
    score.append(int(input()))

dp = [0] * (n+1)
for i in range(1, n+1):
    if i == 1:
        dp[i] = score[i]
    elif i == 2:
        dp[i] = score[i-1] + score[i] # 최대값
    else:
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[n])