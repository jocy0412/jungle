import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split()) # 6 5
graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(v): # 연결된 그룹의 노드들 방문
    visited[v] = True
    for i in graph[v]:
        if not visited[i]: # visited index가 graph의 노드 번호가 되고 그 번호에 방문하지 않았다면
            dfs(i) #  dfs를 실행하여 방문 처리

for j in range(1, len(visited)) :
    if visited[j] == False :
        dfs(j) # 방문하지 않은 연결된 그룹 노드 탐색
        count = count + 1 # 연결된 그룹이 확인되면 + 1개 추가

print(count)