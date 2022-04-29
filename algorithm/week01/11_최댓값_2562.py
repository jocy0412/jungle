import sys
input = sys.stdin.readline

T = int(input())
array = []
for _ in range(T) :
    array.append(input().strip())

for i in array :
    sum = 0
    total = 0
    for j in i :
        if j == 'O' :
            sum += 1
            total += sum
        else :
            sum = 0
    print(total)