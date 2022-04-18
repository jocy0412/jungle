from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

N = int(input()) # 7

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)
vRoot = [0] * (N + 1)

for _ in range(N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1

def dfs(v):
    visited[v] = True
    for i in graph[v] :
        if not visited[i]:
            vRoot[i] = v
            dfs(i)

dfs(1)

for j in range(2, len(vRoot)) :
    print(vRoot[j])