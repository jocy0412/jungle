from sys import stdin
from collections import deque
import queue
input = stdin.readline

N, M = map(int,input().split())
# matrix 배열
matrix = [input().strip() for _ in range(N)]
# 방문경로 배열
visited = [[0] * M for _ in range(N)]

# 좌/우/위/아래 방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 경로 탐색
# queue 방식 사용
queue = [(0,0)]
visited[0][0] = 1

while queue:
    x, y = queue.pop(0)

    if x == N-1 and y == M-1:
        # 최종 경로 도착
        print(visited[x][y])
        break

    for i in range(4):
        nx = x + dx[i] # 현재 위치 x에서 dx만큼 이동할 좌표
        ny = y + dy[i] # 현재 위치 y에서 dy만큼 이동할 좌표
        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and matrix[nx][ny] == '1': # 방문한 적이 없고 이동할 수 있으면
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))