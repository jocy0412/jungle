import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    A, B = list(map(str, input().split()))
    A_int = int(A)
    result = ''
    for j in B :
        result += j*A_int
    print(result)