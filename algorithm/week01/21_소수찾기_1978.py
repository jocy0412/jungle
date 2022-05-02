import sys
input = sys.stdin.readline

A = int(input())

arr = list(map(int, input().split()))
result = 0
for i in arr :
    count = 0
    if i == 1 :
        continue
    for j in range(1, i+1):
        if (i % j) == 0:
            count += 1
    if count == 2:
        result += 1
print(result)