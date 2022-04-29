# 강의실 개수만 구했으~
import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 28
rooms = []
for i in range(N):
    rooms.append(list(map(int, input().split())))

rooms = sorted(rooms, key = lambda x: x[2])
data = [0] * (N+1)

for room in rooms:
    num, start, end = room
    for i in range(start, end + 1) :
        dp[i] += 1
    data[num] = max(dp)

print('필요한 강의실 출력')
print(max(dp))

print('강의 끝나는 순서대로 출력')
print(rooms)