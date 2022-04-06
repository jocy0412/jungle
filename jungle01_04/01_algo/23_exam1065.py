# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

num = int(input())

hansu = 0
for i in range(1, num+1):
    num_list = list(map(int, str(i))) # int는 iterable이 아니므로 str(i)로 변환
    if i < 100:
        hansu += 1
    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
        hansu += 1

print(hansu)