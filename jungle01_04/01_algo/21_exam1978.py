# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데
# 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

n = int(input())
numbers = map(int, input().split())
sosu = 0
for num in numbers:
    error = 0
    if num > 1 :
        for i in range(2, num):  # 2부터 n-1까지
            if num % i == 0: # num을 2부터 n-1까지 나눈 나머지가 0이면 error 증가
                error += 1
        if error == 0:
            sosu += 1  # error가 없으면 소수.
print(sosu)