import sys
sys.setrecursionlimit(10**6)
from copy import deepcopy
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def icebreak() :
    global matrix
    result = deepcopy(matrix)

    for x in range(1, N-1) :
        for y in range(1, M-1) :
            if matrix[x][y] != 0 : # 빙산이 0이 아닌 것들 중에서
                for i in range(4) : # 4방향에 0인 갯수를 체크해서
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if matrix[nx][ny] == 0 : # 0 이면
                        result[x][y] = result[x][y] - 1 if result[x][y] > 0 else 0  # 빙산을 녹인다

    matrix = deepcopy(result) # 다 돌리고나서 원본에 반영(뮤터블, 이뮤터블 카피방법)

def dfs(x,y) :
    visited[x][y] = True
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if not visited[nx][ny] and matrix[nx][ny] :
            dfs(nx,ny)

year = 0

while True :
    count = 0
    icebreak()
    visited = [[0] * M for _ in range(N)]
    for j in range(1, N-1) :
        for k in range(1, M-1) :
            if not visited[j][k] and matrix[j][k] :
                dfs(j,k)
                count = count + 1

    year = year + 1

    if count > 1:
        print(year)
        break
    elif count == 0 :
        print(0)
        break