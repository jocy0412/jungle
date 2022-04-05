# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    L = merge_sort(arr[:mid]) # 분할
    R = merge_sort(arr[mid:]) # 분할
    mer = []

    i = 0
    j = 0
    # 0405 여기부터 이해하기
    while i < len(L) and j < len(R): # 정렬 및 결합
        if (L[i] > R[j]):
            mer.append(R[j])
            j += 1
        else:
            mer.append(L[i])
            i += 1

    if i != len(L):
        mer += L[i:]
    if j != len(R):
        mer += R[j:]
    return mer

mer = merge_sort(arr)
for i in mer:
    print(i)

# 병합 정렬
# 1. 데이터를 절반씩 나누어 끝까지 갔다가(분할)
# 2. 다시 절반씩 합치면서 그안에서 정렬(정복)