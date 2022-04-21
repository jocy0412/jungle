import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split()) # 3 3
matrix = [list(map(int,input().split())) for _ in range(N)]
S, X, Y = map(int,input().split()) # 2 3 2

# 좌/우/위/아래 방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1번 돌렸을 경우
for _ in range(S) :
    visited = [[0] * K for _ in range(N)]
    for x in range(N) :
        for y in range(N) :
            for k in range(1, K + 1):
                if matrix[x][y] == k and visited[x][y] == 0:
                    visited[x][y] = 1
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0 <= nx < N and 0 <= ny < N:
                            if not visited[nx][ny] and matrix[nx][ny] == 0 :
                                matrix[nx][ny] = k
                                visited[nx][ny] = 1
                    # print('정보')
                    # print(*matrix, sep='\n')

print(matrix[X-1][Y-1])

# 시간초과 나옴