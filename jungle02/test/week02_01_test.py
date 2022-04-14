import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

result = []
answer = []
def solution(x, y, N) :
    color = paper[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != paper[i][j] :
                answer.append(f'({color})')
                # 왼쪽에서 오른쪽으로 위에서 아래 순서로 1,2,3,4
                solution(x, y, N//2) # 1
                solution(x+N//2, y, N//2) # 2
                solution(x, y+N//2, N//2) # 3
                solution(x+N//2, y+N//2, N//2) # 4
                return
    if color == 0 :
        answer.append(0)
    else :
        answer.append(1)


solution(0,0,N)