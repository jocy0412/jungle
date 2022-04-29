import sys
input = sys.stdin.readline

T = int(input())

d = [0] * 101
d[0] = 1
d[1] = 1
d[2] = 1
d[3] = 2
d[4] = 2

for i in range(0,T) :
    N = int(input())
    for i in range(5, N+1) :
        d[i] = d[i-1] + d[i-5]
    print(d[N-1])
