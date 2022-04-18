# 문제
# 그래프의 정점의 집합을 둘로 분할하여,
# 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
# 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.

# 그래프가 입력으로 주어졌을 때,
# 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.

# 입력
# 입력은 여러 개의 테스트 케이스로 구성되어 있는데,
# 첫째 줄에 테스트 케이스의 개수 K가 주어진다.
# 각 테스트 케이스의 첫째 줄에는
# 그래프의 정점의 개수 V와 간선의 개수 E가 빈 칸을 사이에 두고 순서대로 주어진다.
# 각 정점에는 1부터 V까지 차례로 번호가 붙어 있다.

# 이어서 둘째 줄부터 E개의 줄에 걸쳐 간선 대한 정보가 주어지는데,
# 각 줄에 인접한 두 정점의 번호 u, v (u ≠ v)가 빈 칸을 사이에 두고 주어진다.

# 2    K
# 3 2  V : 정점 3개 E : 간선 2개

# 1 3
# 2 3
# 4 4

# 1 2
# 2 3
# 3 4
# 4 2

# 출력
# K개의 줄에 걸쳐 입력으로 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력한다.

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

# dfs
def dfs(v, group):
    visited[v] = group # 방문한 노드에 group 할당
    for i in graph[v]:
        if visited[i] == 0: # 아직 안 가본 곳이면 방문
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[v]: # 방문한 곳인데, 그룹이 동일하면 False
            return False
    return True

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)] # 빈 그래프 생성
    visited = [0] * (V+1) # 방문한 정점 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b) # 무방향 그래프
        graph[b].append(a) # 무방향 그래프

    bipatite = True

    for i in range(1, V+1):
        if visited[i] == 0: # 방문한 정점이 아니면, dfs 수행
            bipatite = dfs(i, 1)
            if not bipatite:
                break

    print('YES' if bipatite else 'NO')