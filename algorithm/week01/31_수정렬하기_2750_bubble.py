import sys
input = sys.stdin.readline

T = int(input())

data = [int(input()) for i in range(T)] # [5,2,3,4,1]

for i in range(T): # 0,1,2,3,4
    for j in range(0, T-1): # 0,1,2,3,4
        temp = 0
        if data[j] > data[j+1] :
            temp = data[j]
            data[j] = data[j+1]
            data[j+1] = temp

for i in data :
    print(i)