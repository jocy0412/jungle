import graphlib
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split()) # 6 5
graph = [[] for _ in range(N + 1)] # 노드의 연결 요소를 입력, 노드 번호별 공간이 필요하므로 2차원 배열 사용

visited = [False] * (N + 1) # 노드별로 방문여부만 체크하면 되기 때문에 1차원 배열 사용!

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs (n) :
    visited[n] = True
    for j in graph[n] : # 현재 노드와 연결된 요소들 탐색
        if not visited[j] : # 연결된 요소를 방문하지 않았다면
            dfs(j) # 해당 노드 탐색


for j in range(1, len(visited)) :
    if not visited[j] :
        dfs(j) # 연결된 요소가 끝나지 않으면 dfs가 재귀적으로 호출되서 count가 안되고
        count = count + 1 # 재귀적인 dfs 호출이 끝나면 count + 1

print(count)
