from sys import stdin
from collections import deque
input = stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)] # 연결 그래프

for _ in range(M):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
def dfs(x) :
    visited[x] = True
    print(x, end=' ')
    for i in graph[x] :
        if not visited[i] :
            dfs(i)

dfs(V)

visited = [False] * (N + 1)

def bfs(x) :
    visited[x] = True
    queue = deque([x])
    while queue :
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

bfs(V)