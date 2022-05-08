import sys

def main() :
    input = sys.stdin.readline
    N, M = list(map(int, input().split()))
    treeList = list(map(int, input().split()))

    start, end = 1, max(treeList)

    while start <= end :
        mid = (start + end) // 2 # mid는 자르는 크기

        result = 0 # 목표크기
        for i in treeList :
            if i >= mid :
                result += i - mid

        if result >= M : # 결과크기가 목표크기보다 크면
            start = mid + 1
        else :
            end = mid - 1

    print(end)
main()