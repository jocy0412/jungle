import sys
input = sys.stdin.readline

target = input().rstrip()
explosion = input().rstrip()
stk = []

for i in range(len(target)):
    stk.append(target[i])
    if stk[-1] == explosion[-1]:
        if ''.join(stk[len(stk)-len(explosion):]) == explosion: # 비교 범위를 최소한으로 축소해야 함
            # stk[(스텍의 길이 - 폭팔문자 길이)의 숫자 부터]
            j = len(explosion)
            while j != 0:
                stk.pop()
                j -= 1
                if not stk:
                    break

if not stk:
    print('FRULA')
else:
    print(''.join(stk))
