import sys
from collections import deque
input = sys.stdin.readline

def bfs() :
    queue = deque()
    queue.append(N)

    while queue :
        x = queue.popleft()
        if x == K :
            print(dist[x])
            break
        for nx in (x - 1, x + 1 , x * 2): # nx = 4, 6, 10
            if 0 <= nx <= MAX and not dist[nx] :
                dist[nx] = dist[x] + 1
                queue.append(nx) # q = deque([4, 6, 10])

MAX = 10**5
dist = [0] * (MAX + 1) # 이동거리 체크

N, K = map(int, input().split())

bfs()