import sys
input = sys.stdin.readline

N, K = map(int,input().split()) # 2 7
data = list(map(int,input().split())) # 2 3 2 3 1 2 7
concent = []
count = 0
for i in range(K):
    if data[i] in concent :
        continue
    if len(concent) < N :
        concent.append(data[i])
        continue
    idxs = []
    for j in range(N):
        try: # 현재 플러그에 꽂힌 것 중에 다음 사용 순서에 없거나, 가장 멀리 있는 것
            idx = data[i:].index(concent[j])
            # data[4:].index(concent[0]) -> [5]위치에 1 존재
            # data[4:].index(concent[1]) -> data내에 없으므로 except의 101
        except :
            idx = 101
        idxs.append(idx)

    concent_out = idxs.index(max(idxs))
    del concent[concent_out]
    concent.append(data[i])
    count += 1

print(count)