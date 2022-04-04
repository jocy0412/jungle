
# 나눗셈 후 소수점 이하 표시하는 / 연산자
print(7/3)

# 나눗셈 후 소수점 이하를 버리는 // 연산자
print(7//3)

# 1) 함수 기능
# split()은 문자열을 나눠주는 함수입니다.
# list()는 자료형을 리스트형으로 변환해주는 함수입니다.
# map()은 맵 객체를 만들기 때문에, 리스트형으로 바꿔주기 위해서 list()로 감싸줍니다.

# 1-2) \n은 len에서 한개로 카운트
# inData = "OOXXOXXOOO\n" 10개라고 생각할 수 있지만
# print(len(inData)) \n 포함하여 11개

# 2-1)리스트의 모든 요소를 정수로 변환
#  a = [1.2, 2.5, 3.7, 4.6]
#  for i in range(len(a)):
#      a[i] = int(a[i])
#  print(a) # [1, 2, 3, 4]

# 2-2)map을 사용하여 리스트의 모든 요소를 int로 변환
# a = [1.2, 2.5, 3.7, 4.6]
# a = list(map(int, a))
#  print(a) # [1, 2, 3, 4]

# 3) 임의의 개수의 정수를 한줄에 입력받아 배열에 한번에 받는법
# data = list(map(int,sys.stdin.readline().split()))


# data가 가진 요소를 하나씩 꺼내오는 것
# data = [5,9,2,8]
# for i in data :
#     print(i)

# data의 길이만큼 iterable객체를 만들어 그 안에 있는 요소를 하나씩 꺼내오겠다
# data = [5,9,2,8]
# for i in range(len(data)) :
    # print(i)