# 준서가 여행에 필요하다고 생각하는 N개의 물건이 있다.
# 각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 준서가 V만큼 즐길 수 있다.
# 아직 행군을 해본 적이 없는 준서는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다. 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

# 입력
# 첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과
# 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.

# 입력으로 주어지는 모든 수는 정수이다.
import sys
input = sys.stdin.readline()

n, k = map(int, input().split())

# 아이템의 인덱스 - (무게, 가치) 튜플 사전
dic = {}
for i in range(n) :
    w, v = map( int, input().split() )
    dic[i] = (w, v)

print(dic)
# {0: (6, 13), 1: (4, 8), 2: (3, 6), 3: (5, 12)}


# 칼럼의 경우 무효칸을 맨 앞에 삽입하여, 칼럼 값이 실제 무게와 같이 형성되게 만듬
lst = [ [0] * (k+1) for _ in range(n) ]

# dynamic programming 을 위해, 첫 번째 행 설정
firstTuple = dic[0]
firstW, firstV = firstTuple

# 첫번째 칼럼 1 ~ 무게 한도까지 값 초기화
for i in range(1, k+1) :
    if firstW <= i :
        lst[0][i] = firstV
    else :
        lst[0][i] = 0

# dynamic programming 실시
    # 이번 항목을 포함할 수 없다면, 이전 항목을 포함한 것 까지의 최댓값 취하기
    # 이번 항목을 포함할 수 있다면
        # 1. 할 수 있어도 하지 않은 경우
        # 2. 포함하고, 정해진 무게한도로부터, 이번 항목의 무게를 제외하고, 이전 항목까지의 해당 무게 시의 최댓값
            # : value + lst[r-1][c-weight]

for r in range(1, n) :
    weight, value = dic[r] # 아이템별 무게, 가치
    for c in range(1, k+1):
        if weight <= c : # 현재 아이템 무게보다 최대 무게가 클 경우
            lst[r][c] = max(
                              lst[r-1][c],
                              value + lst[r-1][c-weight]
                                                            )
        else :
            lst[r][c] = lst[r-1][c]

# dp array의 마지막 엔트리 프린트
print( lst[-1][-1] )