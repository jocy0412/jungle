import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int,input().split()) # 3 3
matrix = []
virus = []
for i in range(N) :
    matrix.append(list(map(int,input().split())))
    for j in range(N) :
        if matrix[i][j] != 0 :
            virus.append((matrix[i][j], i, j)) # virus 가 있는 초기값과 좌표 설정
S, X, Y = map(int,input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(s, X, Y) : # 2 3 2
    queue = deque(virus)
    count = 0
    while queue :
        if count == s :
            break
        for _ in range(len(queue)) :
            prev, x, y = queue.popleft()
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                # 조건문 1번 방식 : nx와 ny가 범위 내에 전체적으로 들어오면 실행
                # if 0 <= nx < N and 0 <= ny < N :
                #     if matrix[nx][ny] == 0 :
                #         matrix[nx][ny] = matrix[x][y]
                #         queue.append((matrix[nx][ny], nx, ny))

                # 조건문 2번 방식 : nx와 ny가 범위 밖인게 1개라도 있으면 아래가 실행 안됨
                if nx < 0 or nx >= N or 0 > ny or ny >= N :
                    continue
                if matrix[nx][ny] == 0 :
                    matrix[nx][ny] = matrix[x][y]
                    queue.append((matrix[nx][ny], nx, ny))
        count += 1
    return matrix[X-1][Y-1]

virus.sort()
print(bfs(S, X, Y))
