import sys
# data = list(map(int,sys.stdin.readline().split()))
# print(data)

# a, b = int(input()).split()
# a, b = int(input().split()) # int 함수는 리스트는 정수형으로 바꾸어줄 수가 없다.

# print(a)
# print(b)

# name = "BlockDMask"
# reverse_name = ''

# for c in name:
#     reverse_name = c + reverse_name
#     print(reverse_name)

# print(f'name : {name}')
# print(f'reverse : {reverse_name}')

# a,b  = map(int,sys.stdin.readline().split()) # 123 456
# print(type(a)) # <class 'int'>
# print(a) # 123
# print(type(b)) # <class 'int'>
# print(b) # 456

# data = map(int,sys.stdin.readline().split()) #123
# print(type(data)) # <class 'map'>
# print(data) # <map object at 0x100711d30>

# Case 1
# a = sys.stdin.readline() # The Curious Case of Benjamin Button
# print(a) #The Curious Case of Benjamin Button\n
# print(len(a)) #36

# Case 2
# a = sys.stdin.readline().split() # The Curious Case of Benjamin Button
# print(a) # ['The', 'Curious', 'Case', 'of', 'Benjamin', 'Button']
# print(len(a)) # 6

# Case 3
# a = sys.stdin.readline().split() # 123 456 789
# print(a) ['123', '456', '789']
# print(len(a)) # 3

# Case 4
# a = list(map(str,sys.stdin.readline().split())) # 123 456 789
# print(a) # ['123', '456', '789']
# print(len(a)) # 3

# # Case 5
# a = list(map(int,sys.stdin.readline().split())) # 123 456 789
# print(a) # [123, 456, 789]
# print(len(a)) # 3

# a,b,c = map(int,sys.stdin.readline().split()) # 123 456 789
# print(a) # 123
# print(b) # 456
# print(c) # 789

# a = list(map(str, range(10)))
# print(a)

# a = input().split()    # input().split()의 결과는 문자열 리스트
# x = map(int, a)        # 리스트의 요소를 int로 변환, 결과는 맵 객체
# a, b = x

# print('x는',x)
# print('a는',a)
# print('b는',b)

def recursive(m):
    print("_" * (4 * (n - m)) + '"재귀함수가 뭔가요?"')

    if not m:
        print("_" * (4 * (n - m)) + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        print("_" * (4 * (n - m)) + "라고 답변하였지.")
        return

    print("_" * (4 * (n - m)) + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
    print("_" * (4 * (n - m)) + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print("_" * (4 * (n - m)) + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
    recursive(m - 1)
    print("_" * (4 * (n - m)) + "라고 답변하였지.")


n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursive(n)