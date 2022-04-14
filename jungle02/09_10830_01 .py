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
def matrix_mult(A, B):
    result = [[0] * (len(A)) for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            for k in range(len(B[0])):
                result[i][k] += A[i][j] * B[j][k]
    return result


def matrix_pow(A, n):
    if n == 1:
        return A
    if n % 2 == 0:
        result = matrix_pow(A, n//2)
        return matrix_mult(result, result)
    else:
        result = matrix_pow(A, n-1)
        return matrix_mult(result, A)