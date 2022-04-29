import sys
input = sys.stdin.readline

x = int(input().strip())

d = [0] * 1000

d[0] = 0
d[1] = 1

for i in range(2, x+1):
    d[i] =  d[i-1] + d[i-2]

print(d[x])
