# 문제
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.

# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.

# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)

# 출력
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# a b v
# 2 1 5
import sys
data = list(map(int,sys.stdin.readline().split()))

a = data[0] # 낮에 올라간 거리 : 2
b = data[1] # 밤에 내려간 거리 : 1
v = data[2] # 목표 거리 : 5
move = (a - b)
total = 0
day_count = 1
# print(a,b,v)
if a == v :
    print(day_count)
else :
    total += a
    while total < v :
        total += move
        day_count += 1
    print(day_count)