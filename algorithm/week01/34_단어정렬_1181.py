import sys
input = sys.stdin.readline

T = int(input())
data = [input().strip() for i in range(T)]

print(data)
print('0번값 길이',len(data[0]))
print('1번값 길이',len(data[1]))
print('2번값 길이',len(data[2]))

# set()
# 중복 제거 후에