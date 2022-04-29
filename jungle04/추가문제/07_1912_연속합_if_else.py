import sys
input = sys.stdin.readline

N = int(input()) # 10
data = list(map(int, input().split()))
dp = [0] * (N)
dp[0] = data[0]

for i in range(1, N) :
    if data[i] < dp[i-1] + data[i] :
        dp[i] = dp[i-1] + data[i]
    else :
        dp[i] = data[i]

print(max(dp))
# print(dp)