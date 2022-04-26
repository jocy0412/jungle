import sys
input = sys.stdin.readline

word1, word2 = input().strip(), input().strip()
line1, line2 = len(word1), len(word2)
cache = [0] * line2

for i in range(line1): # 0번 ~ 5번(6개)
    cnt = 0
    for j in range(line2): # 0번 ~ 5번(6개)
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))