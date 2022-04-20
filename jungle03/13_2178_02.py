from sys import stdin
import queue
input = stdin.readline

N, M = map(int,input().split())
matrix = [input().strip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = [(0, 0)]
visited[0][0] = 1

while queue :
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4) :
        nx = x + dx[i] # 현재 위치 x에서 dx만큼 이동할 좌표
        ny = y + dy[i] # 현재 위치 y에서 dy만큼 이동할 좌표

        if nx < 0 or nx >= N or ny < 0 or ny >= M :
            continue

        if visited[nx][ny] == 0 and matrix[nx][ny] == '1' : # 방문한적이 없고 이동 가능하면
            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx,ny))

# print(*matrix, sep='\n')
# print(*visited, sep='\n')