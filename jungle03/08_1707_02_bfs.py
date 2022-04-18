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

### bfs
import collections
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)] # 빈 그래프 생성
    visited = [0] * (V+1) # 방문한 정점 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b) # 무방향 그래프
        graph[b].append(a) # 무방향 그래프


    q = collections.deque()
    group = 1
    bipatite = True
    for i in range(1, V+1):
        if visited[i] == 0: # 방문하지 않은 정점이면 bfs 수행
            q.append(i)
            visited[i] = group
            while q:
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0: # 방문하지 않은 정점이면 큐에 삽입
                        q.append(w)
                        visited[w] = -1 * visited[v] # 현재 노드와 다른 그룹 지정
                    elif visited[v] == visited[w]: # 이미 방문한 경우, 동일한 그룹에 속하면 False
                        bipatite = False

    print('YES' if bipatite else 'NO')