# 1182 - 부분수열의 합/ 재귀함수 / Best!
N, S = map(int, input().split()) # N=5 S=0
A = tuple(map(int, input().split())) #( -7 -3 -2 5 8 )

ans = [0]
def solve(i=0, s=0):
    if i == N:
        if s == S:
            ans[0] += 1
        return
    solve(i+1, s+A[i])
    solve(i+1, s)
solve()
print(ans[0]) if S else print(ans[0]-1)