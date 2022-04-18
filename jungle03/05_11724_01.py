from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

N, M = map(int, input().split()) # 6 5
graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

for j in range(1, len(visited)) :
    if visited[j] == False :
        dfs(j)
        count = count + 1

print(count)