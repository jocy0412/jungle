from collections import deque
import sys
input = sys.stdin.readline

def bfs(node):
    queue = deque()
    queue.append(node)

    while queue :
        node = queue.popleft()

        for n in graph[node]:
            if check[n] == 0:
                check[n] = check[node] + 1
                queue.append(n)

N = int(input()) # 9
A, B = map(int,input().split()) # 7 3
T = int(input()) # 7

graph = [[] for _ in range(N + 1)]
check = [0] * (N + 1)

for _ in range(T) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(A)
print(check[B] if check[B] > 0 else -1)