# 1. 소수 판별(에라토스테네스의 체) > True or False
def is_prime(n) :
    prime = [False,False] + [True] * n
    for i in range(2, int((n+1)**0.5)+1):
        if prime[i] :
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime
# 2. n까지의 소수 목록 산출
def get_prime(n):
    prime = [False,False]+ [True] * n
    for i in range(2, int((n+1)**0.5)+1):
        if prime[i] :
            for j in range(2*i, n+1, i):
                prime[j] = False
    return [k for k in range(2,n) if prime[k] == True]