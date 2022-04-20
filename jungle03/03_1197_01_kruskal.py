import sys
input = sys.stdin.readline

V, E = map(int, input().split()) # 3 3
parent = [i for i in range(V+1)] # 싸이클 테이블, 연결요소중 가장 작은 값, 처음에는 자기 자신을 저장
Elist = [] # 간선들의 정보를 모으는 곳
answer = 0

for _ in range(E):
    Elist.append(list(map(int, input().split())))
    # 입력 : 정점A 정점B 가중치C
    # 1 2 1
    # 2 3 2
    # 1 3 3

Elist.sort(key=lambda x: x[2]) # 가중치 기준으로 정렬

def find_parent(x) :
    if parent[x] != x :
        parent[x] = find_parent(parent[x]) # 경로 압축 기법 : 찾기 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신
    return parent[x]

for start, end, cost in Elist :
    sRoot = find_parent(start)
    eRoot = find_parent(end)
    if sRoot != eRoot :
        # union_parent 기능 : 두 원소가 속한 집합을 합침
        if sRoot > eRoot : # 더 큰 번호에 해당하는 루트 노드의 부모를 작은 번호로 변경
            parent[sRoot] = eRoot
        else: # 시작 루트가 종료 루트보다 작으면 종료 루트값을 시작 루트값으로 연결
            parent[eRoot] = sRoot
        answer += cost

        # 순서가 중요하지 않기 때문에 아래와 같이 사용해도 되긴하지만 위와 같이 관행적으로 사용
        # parent[sRoot] = eRoot
        # answer += cost
print(answer)