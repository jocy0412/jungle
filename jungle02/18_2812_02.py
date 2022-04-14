# 문제
# N자리 숫자가 주어졌을 때, 여기서 숫자 K개를 지워서 얻을 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ K < N ≤ 500,000)

# 둘째 줄에 N자리 숫자가 주어진다. 이 수는 0으로 시작하지 않는다.

# 출력
# 입력으로 주어진 숫자에서 K개를 지웠을 때 얻을 수 있는 가장 큰 수를 출력한다

import sys

N, K = map(int,sys.stdin.readline().split()) # 4 2
nums = list(map(int,sys.stdin.readline().strip())) # 1924를 넣으면 [1,9,2,4] 로 추출

result = []
count = K

for i in range(N) :
    while 0 < count and result :
        if result[len(result)-1] < nums[i]:
            result.pop()
            count -= 1
        else :
            break
    result.append(nums[i])

# for j in result : # 전부 9일경우 K가 소모되지 않아서 범위를 지정해주는게 필요
#     print(j,end='')

for j in range(N-K):
    print(result[j],end="")