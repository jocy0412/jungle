# matrix를 0으로 만들면서 업데이트해서 visited 안쓰는 방법 사용해볼것

from collections import deque
import queue
# 노드의 개수와 간선의 개수 입력
N = int(input())
matrix = [input().strip() for _ in range(N)]

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
visited = [[0] * (N)  for _ in range(N)]

# 좌/우/위/아래 방향 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

countList = []

for x in range(N) :
    for y in range(N) :
        if matrix[x][y] == '1' and visited[x][y] == 0 :

            queue = deque()
            queue.append((x,y))
            visited[x][y] = 1
            count = 1

            while queue :
                a, b = queue.pop()
                for i in range(4):
                    nx = a + dx[i] # 현재 위치 x에서 dx만큼 이동할 좌표
                    ny = b + dy[i] # 현재 위치 y에서 dy만큼 이동할 좌표
                    if 0 <= nx < N and 0 <= ny < N:
                        if visited[nx][ny] == 0 and matrix[nx][ny] == '1':
                            visited[nx][ny] = 1
                            count += 1
                            queue.append((nx, ny))

            countList.append(count)

countList.sort()
print(len(countList))
print(*countList, sep='\n')

# print(*visited, sep='\n')
# print(countList)
