import sys, random
input = sys.stdin.readline
N = int(input())

p_list = []

for i in range(N) :
    comment = list(map(str, input().split()))

    if comment[0] == 'push' :
        p_list.append(comment[1])
    elif comment[0] == 'top' :
        if len(p_list) == 0 :
            print(-1)
        else :
            print(p_list[-1])
    elif comment[0] == 'size' :
        print(len(p_list))
    elif comment[0] == 'empty' :
        if len(p_list) == 0 :
            print(1)
        else :
            print(0)
    elif comment[0] == 'pop' :
        if len(p_list) == 0 :
            print(-1)
        else :
            print(p_list.pop())