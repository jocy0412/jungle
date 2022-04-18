import sys

N = int(sys.stdin.readline())
image = [sys.stdin.readline().rstrip() for _ in range(N)]
result = []

def recursion(N, x, y) :
    color = image[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != image[i][j] :
                result.append('(')
                # 왼쪽에서 오른쪽으로 위에서 아래 순서로 1,2,3,4
                recursion(N//2, x, y) # 1
                recursion(N//2, x, y + N//2) # 3
                recursion(N//2, x + N//2, y ) # 2
                recursion(N//2, x + N//2, y + N//2) # 4
                result.append(')')
                return
    if color == '0' :
        result.append('0')
    else :
        result.append('1')


recursion(N, 0, 0)

print(''.join(result))