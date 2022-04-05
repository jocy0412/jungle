# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

ccnt = 0
scnt = 0
a = [6, 4, 3, 7, 1, 9, 8]
n = len(a)

for i in range(n -1):
    print(f'패스{i+1}')
    for j in range(n-1, i, -1):
        for m in range(0, n-1) :
            print(f'{a[m]:2}' + ('  '
                                    if m != j - 1 else ' +'
                                    if a[j - 1] > a[j] else ' -'
                                ), end='')
        print(f'{a[n - 1]:2}')
        ccnt += 1
        if a[j - 1] > a[j]:
            scnt += 1
            a[j - 1], a[j] = a[j], a[j - 1]
    for m in range(0, n - 1):
        print(f'{a[m]:2}', end='  ')
    print(f'{a[n - 1]:2}')
print(f'비교를 {ccnt}번 했습니다.')
print(f'교환을 {scnt}번 했습니다.')