import sys
# N = str(sys.stdin.readline())
# N = input()

# result = N
# count = 0

# while True :

#     if len(result) == 1 :
#         result = '0' + result
#     plus = str(int(result[0]) + int(result[1])) # 8
#     result = result[-1] + plus[-1]
#     count += 1

#     if result == N :
#         print(count)
#         break


n = int(input()) # 26
result = n # 26
new_num = 0
plus = 0
count = 0

while True :
    plus = n // 10 + n % 10 # int 2 + 6
    new_num = (n % 10) * 10 + plus % 10 # int 60 + 8
    count += 1 # count up
    n = new_num # n = 68
    if new_num == result :
        break

print(count)