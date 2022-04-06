import sys
T = int(input())

hansu = 0
for i in range(1, T+1) :
    num_list = list(map(int,str(i))) # int는 iterable이 아니므로 str(i)로 변환
    print('num_list',num_list)
    if i < 100 :
        hansu += 1
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2] :
        hansu += 1
