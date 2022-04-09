import sys

N = int(sys.stdin.readline()) # 5
N_list = list(map(int,sys.stdin.readline().split()))
N_list.sort() # 1 2 3 4 5

M = int(sys.stdin.readline()) # 5
M_list = list(map(int,sys.stdin.readline().split())) # 1 3 7 9 5

def bin_search(target) :
    left = 0
    right = N - 1 # 4

    while True :
        mid = (left + right) // 2
        if N_list[mid] == target :
            return mid
        elif N_list[mid] < target :
            left = mid + 1
        else :
            right = mid - 1
        if left > right : # while문 해제 조건
            break

for target in M_list :
    if bin_search(target) is None :
        print(0)
    else :
        print(1)

