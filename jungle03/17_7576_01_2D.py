from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int,input().split()) # 6 4
box = [list(map(int,input().split())) for _ in range(N)]
queue = deque([])
dx = [-1, 1, 0, 0] # 상 하
dy = [0, 0, -1, 1] # 좌 우

res = 0


for x in range(N) :
    for y in range(M) :
        if box[x][y] == 1 :
            queue.append([x, y])
def bfs() :
    while queue :
        x, y = queue.popleft()

        for i in range(4) : # 상하좌우에 익지 않은 토마토를 익히기
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0 : # 범위를 벗어나지 않는 애들중에 익지 않은 토마토라면
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in box :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)