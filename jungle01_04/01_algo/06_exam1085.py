# 한수는 지금 (x, y)에 있다. 
# 직사각형은 각 변이 좌표축에 평행하고, 
# 왼쪽 아래 꼭짓점은 (0, 0), 
# 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

import sys
a = []
x, y, w, h = map(int,sys.stdin.readline().split())

a.append(w - x)
a.append(h - y)
a.append(x - 0)
a.append(y - 0)

print((min(a)))

# print(a)
# print(type(a))
# print((min(a)))
# print(type(min(a)))