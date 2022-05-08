from sys import stdin
input = stdin.readline

prime = [False, False] + [True] * (9999)  # true이면 소수
for i in range(2, int(10001 ** 0.5) + 1):
    if prime[i]:
        for j in range(2*i, 10001, i):
            prime[j] = False


t = int(input())
for _ in range(t):
    i = int(input())
    for j in range(i//2,0,-1):
        if prime[j] and prime[i-j]:
            print(j, i-j)
            break