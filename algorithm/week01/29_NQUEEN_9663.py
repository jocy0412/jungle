import sys
input = sys.stdin.readline

N = int(input())

ans = 0
row = [0] * N

def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): # 현재 위치와 같은 줄에 있거나, 현재 위치에서 대각선으로 있을 경우 False
            return False
    return True

def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if check(x):
                n_queens(x+1)

n_queens(0)
print(ans)
