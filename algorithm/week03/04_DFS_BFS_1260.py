import sys
input = sys.stdin.readline
from collections import deque
def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(n):
    visited[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1) :
    graph[i].sort()

visited = [False] * (N + 1)
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)