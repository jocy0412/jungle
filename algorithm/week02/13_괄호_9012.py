import sys
input = sys.stdin.readline
N = int(input())

comment = 0
stack = []
res = 0
for i in range(N) :
    comment = int(input())
    if comment == 0 :
        stack.pop()
    else :
        stack.append(comment)

for i in stack :
    res += i
print(res)