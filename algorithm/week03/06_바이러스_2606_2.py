import sys
input = sys.stdin.readline

def dfs(v) :
    visited[v] = True
    for i in graph[v]:
        if not visited[i] :
            dfs(i)

T = int(input())
N = int(input())

graph = [[] for _ in range(T + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, T + 1) : # 노드 별로 무작위로 데이터값이 들어갔을 수도 있기 때문에 순서를 정렬
    graph[i].sort()

visited = [False] * (T + 1)
dfs(1)

count = -1 # 1번 컴퓨터를 통해서 걸리는 것이기 때문에 1번 컴퓨터는 뺀다

for i in range(1, len(visited)):
    if visited[i] == True :
        count += 1

print(count)