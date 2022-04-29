import sys
input = sys.stdin.readline

A = str(input().strip())
B = str(input().strip())

for i in range(2,-1,-1) :
    print(int(B[i])*int(A))
print(int(B)*int(A))