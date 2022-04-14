# 문제
# 크기가 N*N인 행렬 A가 주어진다.
# 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니,
# A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

# 입력
# 첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

# 둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다.
# 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.

#행렬 곱셈 함수
def matrix_mul(a, b):
    result = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += a[i][k] * b[k][j]

    for i in range(N):
        for j in range(N):
            result[i][j] %= 1000

    return result


#2진법으로 변환하여 분할정복 실행
N, B = map(int, input().split()) # 2, 5
matrix = [list(map(int, input().split())) for _ in range(N)] # 1 2
                                                             # 3 4
B = bin(B)[2:] #2진법으로 변환

#단위 행렬
identity_matrix = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

#2진법 자릿수 만큼 제곱 & 제곱한 행렬 끼리 곱해줌
result = identity_matrix[:]
for i in range(len(B)):
    if B[-i-1] == '1':
        temp = matrix[:]
        while i != 0:
            temp = matrix_mul(temp, temp)
            i -= 1
        result = matrix_mul(result, temp)

for row in result:
    print(*row)