import sys
input = sys.stdin.readline

A, B, C = int(input()), int(input()), int(input())

amount = str(A*B*C)
array = [0]*10

for i in range(10):
    for j in amount:
        if i == int(j):
            array[i] += 1

for k in array:
    print(k)