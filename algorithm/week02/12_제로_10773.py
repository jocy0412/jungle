import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    comment = str(input())

    stack = 0
    for i in comment :
        if i == '(' :
            stack += 1
        elif i == ')' :
            stack -= 1
        if stack < 0 :
            print("NO")
            break

    if stack == 0 :
        print('YES')
    elif stack > 0 :
        print('NO')