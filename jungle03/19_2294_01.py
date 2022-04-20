from collections import deque
import sys
# sys.stdin = open("답체크.txt","r")
input=sys.stdin.readline

N, K = map(int, input().split())
coins = list(set(int(input()) for _ in range(N)))
check = [0 for _ in range(K + 1)] ### 중복된 조합 filter해서 빼주는 효과가 있음// 없으면 메모리 초과난다 ..!

def bfs(coins, K):
    queue = deque()
    for coin in coins:
        if coin < K:
            queue.append([coin,1])
            check[coin] = 1

    while queue:
        cum, cnt = queue.popleft()
        if K == cum:
            print(cnt)
            break
        for coin in coins:
            cum1 = cum + coin
            cnt1 = cnt + 1
            if cum1 > K: # 합한 값이 K보다 크면 폐기
                continue
            elif cum1 <= K and check[cum1] == 0: # 합한 값이 목표값 K보다 같거나 작고 중복된 조합이 없을 경우
                check[cum1] = 1 # 중복된 조합 체크에 체크
                queue.append([cum1,cnt1])

    if cum != K:
        print('-1')

bfs(coins,K)