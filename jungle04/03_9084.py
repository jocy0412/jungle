import sys
input = sys.stdin.readline

# 화폐 문제
T = int(input()) # 3

for _ in range(T):
    N = int(input()) # 코인 갯수 2
    coins = list(map(int,input().split()))
    M = int(input()) # 목표값

    dp = [0] * (M + 1)

    dp[0] = 1

    for coin in coins :
        for j in range(M + 1) :
            if j >= coin :
                dp[j] += dp[j - coin]
    print(dp[M])