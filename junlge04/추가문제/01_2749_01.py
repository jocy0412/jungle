import sys
input = sys.stdin.readline

N = int(input()) # 1000

M = 1000000 # M(나눌 수) = 10^6
fibo = [0, 1]
P = M//10*15 # P(주기의 길이) = 1,500,000

for i in range(2,P):
    fibo.append(fibo[i-1]+fibo[i-2])
    fibo[i] %= M

print(fibo[N%P])