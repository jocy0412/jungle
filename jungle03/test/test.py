N, K = map(int,input().split()) # 3 3
matrix = []
virus = []
for i in range(N) :
    matrix.append(list(map(int,input().split())))
    for j in range(N) :
        if matrix[i][j] != 0 :
            virus.append((matrix[i][j], i, j)) # virus 가 있는 초기값과 좌표 설정
            print(virus)
S, X, Y = map(int,input().split())