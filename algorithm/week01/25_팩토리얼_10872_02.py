import sys
input = sys.stdin.readline

T = int(input())
def fact(n) :
    if n > 0:
        return n * fact(n-1)
    return 1
print(fact(T))