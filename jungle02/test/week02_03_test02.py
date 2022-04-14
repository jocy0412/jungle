import sys
import heapq

K, N = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
print(data)

for i in range(N):
    m = data[0] * data[i]
    data.append(m)
    data.sort()
print(data[N-1])