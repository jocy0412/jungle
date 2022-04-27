import sys
input = sys.stdin.readline

T = int(input()) # 2

for _ in range(T): # 2
    N = int(input()) # 5
    data = []
    data = [list(map(int,input().split())) for rank in range(N)]
    data = sorted(data, key=lambda x: x[0])
    answer = []
    answer.append(data[0])
    rank = data[0][1]
    for i in range(1, len(data)):
        if rank > data[i][1] :
            rank = data[i][1]
            answer.append(data[i])
    print(len(answer))