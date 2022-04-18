# 문제
# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다.
# 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다.
# A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.

# 입력
# 첫째 줄에 도시의 개수 , 둘째 줄에는 버스의 개수
# 그리고 셋째 줄부터 M+2줄까지
# 처음에는 그 버스의 출발 도시의 번호, 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다.
# 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.

# 마지막 줄은 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input()) # 5
M = int(input()) # 8

distance = [INF] * (N + 1)  # 거리
graph = [[] for _ in range(N + 1)] # N개의 길에 대한 간선 경로

for _ in range(M) : # 버스 정보 입력
    a, b, c = map(int, input().split()) # a:출발 도시의 번호, b:도착 도시 번호, c:버스 비용
    graph[a].append((b, c))

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    while queue :
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now] : # 현재 위치(now) 기준으로 접근할 수 있는 영역 체크
            cost = dist + i[1]
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

start, end = map(int,input().split()) # 출발점의 도시번호 1, 도착점의 도시 번호 5

dijkstra(start)
print(distance[end])

# 예제 입력
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3 M+2줄