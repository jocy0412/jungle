import graphlib
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input()) # Test case : 2

def dfs(start, group) :
    visited[start] = group;
    for i in graph[start] :
        if not visited[i] :
            if not dfs(i, -group) :
                return False
        elif visited[i] == group :
            return False

    return True


for _ in range(K) :
    V, E = map(int, input().split()) # 정점 개수 V : 3, 간선 개수 E : 2 ,
    graph = [[] for _ in range(V + 1)]
    visited = [False] * (V + 1)
    for __ in range(E) :
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V+1) :
        if visited[i] == False :
            result = dfs(i, 1)
            if not result :
                break

    print("YES" if result else "NO" )