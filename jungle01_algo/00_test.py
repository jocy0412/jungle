# data = "OOXXOXXOOO"
# add = 0
# score = 0

# # data의 길이만큼 iterable객체를 만들어 그 안에 있는 요소를 하나씩 꺼내오겠다
# for i in range(len(data)) :
#     if data[i] == "O" :
#         add += 1
#         score += add
#     else :
#         add = 0

# print(score)


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

for j in range(len(data)) :
    inData = data[j]
    # print(inData) ## 여기부터 \n이 사라지고 줄바꿈 처리됨
    for k in range(len(inData)) :
        print(len(inData))
    #     if inData[k] == "O" :
    #         add += 1
    #         score += add
    #     else :
    #         add = 0
    # print(score)
    # score = 0