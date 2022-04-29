import sys
input = sys.stdin.readline

N = int(input())

rooms = [[0]*2 for _ in range(N)]

for i in range(N):
    num, start, end = map(int, sys.stdin.readline().split())
    rooms[i][0] = num
    rooms[i][1] = start
    rooms[i][2] = end

rooms.sort(key = lambda x: (x[2], x[1]) )

count = 1
end_time = rooms[0][2]
for i in range(1, N):
    if rooms[i][0] >= end_time:
        count += 1
        end_time = rooms[i][1]