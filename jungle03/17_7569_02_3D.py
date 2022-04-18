from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int,input().split()) # 5 3 1
for _ in range(H) :
    box = [list(map(int,input().split())) for _ in range(N)]

queue = deque([])

dh = [-1, 1, 0, 0, 0, 0] # 높이 위 아래
dx = [0, 0, -1, 1, 0, 0] # 상 하
dy = [0, 0, 0, 0, -1, 1] # 좌 우

res = 0

for h in range(H):
    for x in range(N) :
        for y in range(M) :
            if box[h][x][y] == 1 :
                queue.append([h,x,y])
def bfs() :
    while queue :
        h, x, y = queue.popleft()

        for i in range(6) : # 상하좌우에 익지 않은 토마토를 익히기
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and box[nh][nx][ny] == 0 : # 범위를 벗어나지 않는 애들중에 익지 않은 토마토라면
                box[nh][nx][ny] = box[h][x][y] + 1
                queue.append([nh, nx, ny])

bfs()
for i in box :
    for j in i :
        for k in j :
            if k == 0 :
                print(-1)
                exit(0)
    res = max(res, max(k))
print(res - 1)