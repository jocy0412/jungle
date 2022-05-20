import sys
input = sys.stdin.readline
N = int(input())
stick = list(map(int, input().split())) # 6 9 5 7 4
res = [0] * (N)

for i in range(N-1,0,-1) : # 4, 3, 2, 1
    for j in range(i-1,-1,-1) : # 3, 2, 1, 0
        if res[i] == 0 :
            if stick[i] < stick[j] :
                res[i] = j+1
print(" ".join(map(str, res)))