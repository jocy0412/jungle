N = int(input())
N_list = list(map(int, input().split(' ')))
N_list.sort()

M = int(input())
M_list = list(map(int, input().split()))

def bin(target) :
    left = 0
    right = N - 1

    while left <= right :
        mid = (left + right) // 2

        if N_list[mid] == target :
            return True
        elif N_list[mid] < target :
            left = mid + 1
        else :
            right = mid - 1


for target in M_list :
    if bin(target) :
        print(1)
    else :
        print(0)


