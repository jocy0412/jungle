# 음료수 얼려 먹기

# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력 예시
# 3

from sys import stdin, stdout
input = stdin.readline
print = stdout.write

def dfs (x,y) :
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

    if graph[x][y] == 0 : # 현재 노드를 방문하지 않았다면
        graph[x][y] = 1 # 현재 노드를 방문 처리
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y+ 1)
        return True
    return False

# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int,input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 음료수 채우기
result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True : # 현재 위치에서 DFS 수행
            result += 1

print(result)