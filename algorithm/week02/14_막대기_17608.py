import sys
input = sys.stdin.readline
N = int(input())
stick = [int(input()) for _ in range(N)]
stack = stick[-1]
count = 1
for i in range(N-2,-1,-1) :
    if stick[i] > stack :
        stack = stick[i]
        count += 1
print(count)