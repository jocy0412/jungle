import sys
input = sys.stdin.readline

T = int(input()) # 3
for i in range(T):
    N = int(input()) # 2
    coins = list(map(int,input().split())) # 1 2
    M = int(input()) # 1000

    dp = [0] * (M+1) # M+1 개를 곱해야 M원까지 만들 수 있다.
    dp[0] = 1 # 조건 dp[1] = 1 로 잘못 설정함

    for coin in coins :
        for j in range(M+1) : # range 2, M+1 로 잘못 설정
            if j >= coin : # 여기 조건
                dp[j] += dp[j - coin] # dp[j]는 dp[j]에서 추가하는 코인의 갯수만큼 만들 수 있다.
                # dp[3] += dp[3 - 2] # 예를들면 3원을 만드는 케이스는 3원에서 2원을 뺀 1원 케이스를 더해주면 만들 수 있는 케이스가 생긴다.
    print(dp[M])

