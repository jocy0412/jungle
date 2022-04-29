import sys
input = sys.stdin.readline

N, X = map(int, input().split())

A = list(map(int,input().split()))
a_data =[]
for i in A :
    if i < X :
        print(i,end=" ")