import sys
input = sys.stdin.readline

N = int(input()) # 99

dp = [0] * (N + 1)

dp[1] = 0
dp[2] = 1

for i in range(3, N + 1) :
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N]) # 218922995834555169026