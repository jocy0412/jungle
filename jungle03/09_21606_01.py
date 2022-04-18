# 문제
# 아침 산책을 즐기는 서현이는 서울과학고에 입학해서도 아침 산책을 즐기려고 합니다. 서현이는 산책을 위해 서울과학고의 지리를 분석했고, 그 결과 서울과학고를 $N$개의 장소를 $N-1$개의 길이 잇는 트리 형태로 단순화시킬 수 있었습니다. 트리 구조이므로, 모든 장소를 몇 개의 길을 통해 오고갈 수 있습니다.

# 아침 산책은 시작점과 도착점을 정하고, 시작점에서 도착점까지 트리 위의 단순 경로(같은 점을 여러 번 지나지 않는 경로)를 따라 걷게 됩니다. 트리 위의 두 점 사이의 경로는 유일하므로 시작점과 도착점이 정해지면 경로는 유일하게 결정됩니다.

#  $N$개 장소 중에 일부 장소는 실내이며, 나머지 장소는 실외입니다. 서현이는 산책을 시작하기 전부터 운동을 하는 것을 원치 않기 때문에, 산책의 시작점과 끝점은 모두 실내여야 합니다. 또한, 산책 도중에 실내 장소를 만나면 산책을 그만두고자 하는 욕구가 생기기 때문에, 산책 경로 위에 시작점과 끝점을 제외하고 실내 장소가 있으면 안 됩니다.

# 서현이는 매일 다른 산책 경로를 걷고자 합니다. 서로 다른 산책 경로가 몇 가지 있는지 구해 봅시다.

# 입력
# 첫 줄에는 정점의 수 $N$이 주어집니다.

# 1 = 장소 실내
# 0 - 장소 실외

# 5
# 10111
# 1 2
# 2 3
# 2 4
# 4 5

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def calPaths(graph, col) :
    count = 0
    visited = set()

    def dfs(exterior) :
        cnt = 0
        for neighbor in graph[exterior]:
            if col[neighbor] == 1:
                cnt += 1
            else:
                if neighbor not in visited:
                    visited.add(neighbor)
                    cnt += dfs(neighbor)
        return cnt

    for i in range(1, N + 1):
        # 각 실내별 인접한 실내 구하기
        if col[i] == 1:
            for j in graph[i]:
                if col[j] == 1:
                    count += 1
        # 인접한 실외를 한 덩어리로 보고 그 덩어리에 인접한 실내의 수를 구한 뒤
        # 각 덩어리별로 n*(n-1)의 경우의 수를 계산
        else:
            if i not in visited:
                visited.add(i)
                tmp = dfs(i)
                count += tmp * (tmp - 1)

    return count

N = int(input())
col = list(map(int, list("0"+input().strip())))

graph = [[] for _ in range(N + 1)]

for _ in range(1, N):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(calPaths(graph, col))