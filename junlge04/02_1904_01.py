import sys
input = sys.stdin.readline

x = int(input().strip())

d = [0] * 1000001 # dp 개수보다 + 1

d[1] = 1
d[2] = 2

for i in range(3, x+1):
    d[i] =  (d[i-1] + d[i-2]) % 15746 # 나머지 출력을 위해 15746개로 나눔

print(d[x])
