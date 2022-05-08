import sys
input = sys.stdin.readline

# input 입력 받기
n = int(input()) # 5
solution = list(map(int, input().split(' '))) # -2 4 -99 -1 98

# 정렬하기
solution.sort() # -99, -2, -1, 4, 98

# 이중포인터 설정
left = 0
right = n-1
one = 0
two = 0

result = 2e+9+1 # 기준값

while left < right :
    temp = solution[left] + solution[right]
    zero = abs(temp)

    if result > zero :
        result = zero # 96, 3, 100, 1
        one = solution[left] # null, -2, null, -99
        two = solution[right] # null, -1, null, 98

    if temp < 0 :
        left += 1
    else :
        right -= 1

print(one, two)