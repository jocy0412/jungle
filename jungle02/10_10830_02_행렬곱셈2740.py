# 문제
# N*M크기의 행렬 A와 M*K크기의 행렬 B가 주어졌을 때, 두 행렬을 곱하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 행렬 A의 크기 N 과 M이 주어진다. 둘째 줄부터 N개의 줄에 행렬 A의 원소 M개가 순서대로 주어진다. 그 다음 줄에는 행렬 B의 크기 M과 K가 주어진다. 이어서 M개의 줄에 행렬 B의 원소 K개가 차례대로 주어진다. N과 M, 그리고 K는 100보다 작거나 같고, 행렬의 원소는 절댓값이 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄부터 N개의 줄에 행렬 A와 B를 곱한 행렬을 출력한다. 행렬의 각 원소는 공백으로 구분한다.


N,M = map(int,input().split())
matrix1 = []
for _ in range(N):
    matrix1.append(list(map(int,input().split())))
Mb,K = map(int,input().split())
matrix2=[]
for _ in range(Mb):
    matrix2.append(list(map(int,input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]
for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += matrix1[n][m] * matrix2[m][k]

for row in result:
    for num in row:
        print(num,end=' ')
    print()