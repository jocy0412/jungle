import sys
input = sys.stdin.readline
N, K = map(int, input().split())
data = list(input())

stack = []
count = K

for i in range(N) :
    while 0 < count and stack : # 숫자를 뺄 수 있으면서 stack 이 있을 경우
        if stack[len(stack)-1] < data[i] : # 스택보다 선택된 값이 클경우
            stack.pop() # 스택에 들어간 값을 빼고
            count -= 1 # 숫자 뺄 수 있는 카운트를 내리고
        else :
            break
    stack.append(data[i]) # while문이 다 돌면 스택에 들어갈 data[i]값을 넣는다

print(''.join(stack[:N-K]))

# for j in range(N-K):
#     print(stack[j],end='')




# 19224 = 924
# stack = 0 과 data[0] 1 크기를 비교하고 1을 stack에 저장
# stack 1이랑 data[1] 9중에 비교 9를 저장하고 stack 삭제  stack 0
# stack 0이랑 data
