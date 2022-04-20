# 골드 4레벨        최소 스패닝 트리
# 크루스칼 알고리즘
# 유니온 파인드
import sys
input = sys.stdin.readline

def find(a): # 특정 원소가 속한 집합 찾기
    if a == parent[a]: # 루트 노드르 찾을 때까지 재귀 호출
        return a
    parent[a] = find(parent[a])  # 경로 압축
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())

parent = list(range(V + 1)) # 부모 테이블상에서 부모를 자기 자신으로 초기화

edge = [] # 모든 간선을 담을 리스트
sum = 0 # 최종 비용을 담을 변수

for _ in range(E):
    a, b, cost = map(int, input().split())
    edge.append((cost, a, b))

edge.sort(key=lambda x: x[0])

for cost, start, end in edge:
    if find(start) != find(end):
        union(start, end)
        sum += cost

print(sum)