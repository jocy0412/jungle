# import sys
# N = int(sys.stdin.readline())
# paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# print(paper)

explosion = 'C4'

print(len(explosion))
stk = ['m',"i","r","k","o","v","C","4"]
print(len(stk))
print(stk[len(stk)-len(explosion):])

print(''.join(stk))