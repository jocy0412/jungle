from collections import deque # Queue를 사용하기 위한 collection library 사용

N, M = map(int, input().split())

matrix = []

for i in range(N) :
    matrix.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1] # 상하좌우 움직이도록 하는 list

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.pop()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 > nx or nx >= N or 0 > ny or ny >= M  :
                continue
            if matrix[nx][ny] == 0  :
                continue

            if 0 <= nx < N and 0 <= ny < M  :
                if matrix[nx][ny] == 1 :
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append((nx, ny))

    return matrix[N-1][M-1]

print(bfs(0,0))
print(matrix)