from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = -1

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

for j in range(1, len(visited)) :
    if visited[j] == True :
        count = count + 1

print(count)