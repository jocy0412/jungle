import sys
input = sys.stdin.readline

n = int(input())
t = []
for i in range(n):
    t.append(list(map(int, input().split())))
k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
    k += 1
print(max(t[n - 1]))
# 7
# 10 15
# 18 16 15
# 20 25 20 19
# 24 30 27 26 24

# 1. 맨 처음 인덱스는 이전 단계 같은 인덱스에서 더한 값
# 2. 이전 단계 같은 인덱스에서 더한 값이나
#    이전 단계 이전 인덱스 - 1 위치에서 더한 값중 젤큰크기
# 3. 맨 끝 인덱스는 이전 단계 인덱스 -1 위치