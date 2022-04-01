# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
# 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 
# 각 테스트 케이스는 한 줄로 이루어져 있고, 
# 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 
# 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.

import sys
data = []
add = 0
score = 0

n = int(sys.stdin.readline())

for i in range(n) :
    inp = str(sys.stdin.readline()) # \n 텍스트 노출
    # inp = str(sys.stdin.readline().strip()) # \n 텍스트 삭제
    data.append(inp)

# print(data) # 여기까지 \n 붙어서 나와서 strip()을 위에서 처리해줘야하나?

for j in range(len(data)) : # print(len(data[j])) # 보이지 않아도 \n 값을 1로 추가로 카운트 하고 있음
    inData = data[j] # print(inData) ## 여기부터 \n이 사라지고 줄바꿈 처리됨
    for k in range(len(inData)) :
        if inData[k] == "O" :
            add += 1
            score += add
        else :
            add = 0
    print(score)
    score = 0
