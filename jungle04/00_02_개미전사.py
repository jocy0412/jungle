import sys
input = sys.stdin.readline
X = int(input())
data = list(map(int, input().split()))

d = [0] * 1001

d[0] = data[0]
d[1] = max(data[0],data[1])

for i in range(2,X+1) :
    d[i] = max(d[i-1], d[i-2] + data[i])

print(d[X])
# 입력
# 3
# 1 3 1 5