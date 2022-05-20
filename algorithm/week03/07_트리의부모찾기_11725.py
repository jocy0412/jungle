import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            if vRoot[i] == 0 :
                vRoot[i] = v
            dfs(i)

N = int(input())

graph = [[] for _ in range(N + 1)] # 빈 graph 영역 추가
visited = [False] * (N + 1) # 방문 여부 처리
vRoot = [0] * (N + 1) # 방문 노드들의 부모 영역

for _ in range(N-1) : # 노드별로 연결 요소를 입력
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1) : # 노드 별로 무작위로 데이터값이 들어갔을 수도 있기 때문에 순서를 정렬
    graph[i].sort()

dfs(1)

for j in range(2, len(vRoot)) :
    print(vRoot[j])