from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

def dfs(node):
    for n in graph[node]:
        if check[n] == 0:
            check[n] = check[node]+1
            dfs(n)

N = int(input()) # 9
A, B = map(int,input().split()) # 7 3
T = int(input()) # 7

graph = [[] for _ in range(N + 1)]
check = [0] * (N + 1)

for _ in range(T) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(A)
print(check[B] if check[B] > 0 else -1)