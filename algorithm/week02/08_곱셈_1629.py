import sys
input = sys.stdin.readline

# input 입력 받기
A, B, C = map(int, input().split())
d = [0] * (10**5)

d[1] = A

for i in range(2, B+1) :
    if d[i] != 0 :
        continue
    d[i] = d[i-1] * A
print(d[B] % C)