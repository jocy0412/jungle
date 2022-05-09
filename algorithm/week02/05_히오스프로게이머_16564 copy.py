import sys
input = sys.stdin.readline

# input 입력 받기
N, K = map(int, input().split()) # 3 10
level = sorted([int(input()) for _ in range(N)])
start, end = min(level), max(level) + K
res = 0

def count(level, mid) :
    t = 0
    for i in level :
        if i < mid :
            t += mid - i
        else :
            break
    return t


while start <= end :
    mid = (start + end) // 2
    if count(level, mid) <= K :
        res = mid
        start = mid + 1
    else :
        end = mid - 1

print(res)