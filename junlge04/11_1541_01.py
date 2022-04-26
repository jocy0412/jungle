a = input().split('-')
num = []

for i in a:
    cnt = 0
    s = i.split('+') # + 가 있으면 split해서 담아준다
    for j in s: # 나눠진 요소들을 하나씩 더해준다.
        cnt += int(j)
    num.append(cnt)
n = num[0]

for i in range(1, len(num)):
    n -= num[i]
print(n)