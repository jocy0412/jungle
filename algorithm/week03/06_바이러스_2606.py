import sys
input = sys.stdin.readline
from collections import deque
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

T = int(input())
N = int(input())

graph = [[] for _ in range(T + 1)]

for _ in range(N) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, T + 1) :
    graph[i].sort()

visited = [False] * (T + 1)
dfs(1)

count = -1

for j in range(1, len(visited)) :
    if visited[j] == True :
        count = count + 1

print(count)