import sys
# N = str(sys.stdin.readline())
N = input()

result = N
count = 0

while True :

    if len(result) == 1 :
        result = '0' + result
    plus = str(int(result[0]) + int(result[1])) # 8
    result = result[-1] + plus[-1]
    count += 1

    if result == N :
        print(count)
        break