# 못풀었으~

import sys
input = sys.stdin.readline

N = int(input())
matrix = []
dp = [[0] * N for i in range(N)]

for i in range(N) :
    matrix.append(list(map(int,input().split())))

count = 0
x = 0
y = 0
move = matrix[x][y]

if x + move < N :
    matrix[x + move][y]
    move = matrix[x + move][y]
if y + move < N :
    matrix[x][y + move]
    move = matrix[x][y + move]
if x == N and y == N :
    count += 1