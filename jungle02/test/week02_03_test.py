


import sys
import heapq

K, N = map(int,sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
print(data)

for i in range(N):
    m = data[0] * data[i]
    heapq.heappush(data, m)
print(data)

# data = [2, 3, 5 ,7]
# heap = []
# n = int(sys.stdin.readline())
# for _ in range(n):
#   m = int(sys.stdin.readline())
#   if m == 0:
#     if len(heap) == 0:
#       print(0)
#     else:
#       print((-1)*heapq.heappop(heap))
#   else:



# # data = [2, 3, 5 ,7]
# # result = []
# # result.append(data)
# # for i in data :
