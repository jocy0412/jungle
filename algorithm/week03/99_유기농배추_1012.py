import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y) :
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<= nx < N) and (0 <= ny < M) :
            if matrix[nx][ny] == 1 :
                matrix[nx][ny] = -1
                dfs(nx, ny)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split()) # 10 , 8 , 17
    matrix = [[0] * M for _ in range(N) ] # 10, 8
    count = 0

    for _ in range(K) : # 17
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(N) : # N : 8
        for j in range (M) : # N : 10
            if matrix[i][j] > 0 :
                dfs(i, j)
                count += 1

    print(count)
