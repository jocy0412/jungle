import sys
input = sys.stdin.readline
N = int(input())
N_data = list(map(int, input().split()))
N_data.sort()

M = int(input())
M_list = list(map(int, input().split()))

def bin(x):
    start = 0
    end = N - 1
    while start <= end :
        mid = (start + end) // 2
        if N_data[mid] == x:  # 선택된 값과 목표값이 같을 경우
            return True
        elif N_data[mid] < x : # 선택된 값보다 목표값이 클 경우
            start = mid + 1 # 선택값보다 1개 큰 경우에서 다시 검색
        else :
            end = mid - 1 # 선택값보다 1개 작은 경우에서 다시 검색

for i in M_list :
    if bin(i) :
        print(1)
    else :
        print(0)