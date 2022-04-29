import sys
input = sys.stdin.readline

C = int(input())
array = []
for _ in range(C) :
    array.append(list(map(int,input().split())))

for list in array :
    amount = 0 # 합계
    count = 0 # 평균 넘는 학생 수
    people = len(list)-1 # 전체학생수
    for j in range(1,len(list)):
        amount += list[j]
    average = amount/people # 평균
    for i in range(1,len(list)) :
        if list[i] > average :
            count += 1
    rate = (count/people)*100
    print("%0.3f" % rate+'%')