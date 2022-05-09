import sys
input = sys.stdin.readline

# input 입력 받기
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = []

def search(N, x, y) :
    color = matrix[x][y]
    for i in range(x, x + N) :
        for j in range(y, y + N) :
            if matrix[i][j] != color :
                search(N//2, x, y)
                search(N//2, x + N//2, y)
                search(N//2, x, y + N//2)
                search(N//2, x + N//2, y + N//2)
                return
    if color == 0 :
        result.append(0)
    else :
        result.append(1)

search(N, 0, 0)
print(result.count(0))
print(result.count(1))