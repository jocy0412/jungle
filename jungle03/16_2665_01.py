# 미로만들기
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
dx = [-1, 1, 0, 0] # 상 하
dy = [0, 0, -1, 1] # 좌 우

matrix = [input().strip() for _ in range(N)]

q = deque()
q.append((0, 0))
visited = [[-1] * N for _ in range(N)]
visited[0][0] = 0

while q :
    x, y = q.popleft()

    if x == N-1 and y == N-1 :
        print(visited[x][y])
        break

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1: # 전체 범위를 넘지 않고 방문한 적이 없고
            if matrix[nx][ny] == '1' : # 장벽이 없다면
                q.appendleft((nx, ny))
                visited[nx][ny] = visited[x][y]
            else : # 장벽이 있다면 +1 추가
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

# print(visited)
# [
#     '11100110',
#     '11010010',
#     '10011010',
#     '11101100',
#     '01000111',
#     '00110001',
#     '11011000',
#     '11000111'
# ]