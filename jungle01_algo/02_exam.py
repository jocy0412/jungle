import sys
# 1. 한 개의 정수를 입력받을 때
# a = int(sys.stdin.readline())

# 2. 정해진 개수의 정수를 한줄에 입력받을 때
a,b = map(int,sys.stdin.readline().split()) 

# 3. 한줄에 입력받는 케이스
# a,b = input().split()
# a = int(a)
# b = int(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b) 
print(a%b)