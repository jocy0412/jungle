import sys

N = int(sys.stdin.readline()) # 5
total_list = list(map(int,sys.stdin.readline().split()))
total_list.sort() # 8 3 7 9 2

M = int(sys.stdin.readline()) # 3
find_list = list(map(int,sys.stdin.readline().split())) # 5 7 9


def search(target) :
    start = 0
    end = N - 1
    while start <= end :
        mid = (start + end) // 2
        if total_list[mid] == target :
            return True
        elif total_list[mid] < target :
            start = mid + 1
        else :
            end = mid - 1

for target in find_list :
    if search(target) :
        print('yes')
    else :
        print('no')