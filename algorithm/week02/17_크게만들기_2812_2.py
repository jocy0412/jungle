import sys
input = sys.stdin.readline
N, K = map(int, input().split())
data = list(input())

stack = []
count = K

for i in range(N) :
    while 0 < count and stack and stack[-1] < data[i] :
        stack.pop()
        count -= 1
    stack.append(data[i])

for j in range(N-K):
    print(stack[j],end='')



# 19224 = 924
# stack = 0 과 data[0] 1 크기를 비교하고 1을 stack에 저장
# stack 1이랑 data[1] 9중에 비교 9를 저장하고 stack 삭제  stack 0
# stack 0이랑 data
